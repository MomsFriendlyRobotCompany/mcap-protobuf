#!/usr/bin/env python3
# pip install opencv-contrib-python websockets
# pip install websockets numpy opencv-python protobuf
# pip install foxglove-websocket[examples]
#
import asyncio
import sys
import time
from base64 import b64encode
from foxglove_websocket import run_cancellable
from foxglove_websocket.server import FoxgloveServerListener
from foxglove_websocket.server import FoxgloveServer
# from foxglove_schemas_protobuf.CameraCalibration_pb2 import CameraCalibration
from foxglove_schemas_protobuf.RawImage_pb2 import RawImage
from foxglove_schemas_protobuf.SceneUpdate_pb2 import SceneUpdate
from google.protobuf.descriptor_pb2 import FileDescriptorSet
from google.protobuf.descriptor import FileDescriptor
from pyquaternion import Quaternion
import numpy as np
import cv2


bgr2gray = lambda im: cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


# def timestamp(time_ns: int):
#   return Timestamp(seconds=time_ns // 1_000_000_000, nanos=time_ns % 1_000_000_000)

# Function to create a sample image
def create_sample_image():
  img = np.zeros((64, 64), dtype=np.uint8)
  for i in range(64):
    for j in range(64):
      img[i, j] = ((i // 8) + (j // 8)) % 2 * 255
  return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


def build_file_descriptor_set(message_class):
  """
  Build a FileDescriptorSet representing the message class and its dependencies.
  """
  file_descriptor_set = FileDescriptorSet()
  seen_dependencies: Set[str] = set()

  def append_file_descriptor(file_descriptor):
    for dep in file_descriptor.dependencies:
      if dep.name not in seen_dependencies:
        seen_dependencies.add(dep.name)
        append_file_descriptor(dep)
    file_descriptor.CopyToProto(file_descriptor_set.file.add())

  append_file_descriptor(message_class.DESCRIPTOR.file)
  return file_descriptor_set


async def main():
  class Listener(FoxgloveServerListener):
    async def on_subscribe(self, server, channel_id):
      print("First client subscribed to", channel_id)

    async def on_unsubscribe(self, server, channel_id):
      print("Last client unsubscribed from", channel_id)

  async with FoxgloveServer("0.0.0.0", 8765, "example server") as server:
    server.set_listener(Listener())
    chan_id = await server.add_channel(
      {
        "topic": "example_msg",
        "encoding": "protobuf",
        "schemaName": SceneUpdate.DESCRIPTOR.full_name,
        "schema": b64encode(
            build_file_descriptor_set(SceneUpdate).SerializeToString()
        ).decode("ascii"),
        "schemaEncoding": "protobuf",
      }
    )
    image_id = await server.add_channel(
      {
        "topic": "image_msg",
        "encoding": "protobuf",
        "schemaName": RawImage.DESCRIPTOR.full_name,
        "schema": b64encode(
            build_file_descriptor_set(RawImage).SerializeToString()
        ).decode("ascii"),
        "schemaEncoding": "protobuf",
      }
    )

    i = 0
    while True:
      i += 1
      await asyncio.sleep(0.05)
      now = time.time_ns()

      scene_update = SceneUpdate()
      entity = scene_update.entities.add()
      entity.timestamp.FromNanoseconds(now)
      entity.frame_id = "root"
      cube = entity.cubes.add()
      cube.size.x = 1
      cube.size.y = 1
      cube.size.z = 1
      cube.pose.position.x = 2
      cube.pose.position.y = 0
      cube.pose.position.z = 0
      q = Quaternion(axis=[0, 1, 1], angle=i * 0.1)
      cube.pose.orientation.x = q.x
      cube.pose.orientation.y = q.y
      cube.pose.orientation.z = q.z
      cube.pose.orientation.w = q.w
      cube.color.r = 0.6
      cube.color.g = 0.2
      cube.color.b = 1
      cube.color.a = 1

      await server.send_message(chan_id, now, scene_update.SerializeToString())

      frame = create_sample_image()
      height, width, _ = frame.shape

      # img = RawImage(
      #   timestamp=timestamp(now),
      #   frame_id="root",
      #   width=width,
      #   height=height,
      #   encoding="rgb8",
      #   step=width * 3,
      #   # encoding="mono8",
      #   # step=width,
      #   data=frame.tobytes(),
      # )

      img = RawImage()
      img.frame_id = "root"
      img.width = width
      img.height = height
      img.encoding = "rgb8"
      img.step = width*3
      img.timestamp.FromNanoseconds(now)
      img.data = frame.tobytes()

      await server.send_message(image_id, now, img.SerializeToString())


if __name__ == "__main__":
  run_cancellable(main())
