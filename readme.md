# Protobuf and MCAP Testing

## Linux

```bash
apt install -y protobuf-compiler
```

## macOS

```bash
brew install protobuf
brew install mcap
pip install -U protobuf mcap mcap-protobuf-support foxglove-schemas-protobuf
```

## Generate Python Protobuf Messages

```bash
protoc protoc --python_out=gen proto/simple_msg.proto
```

## Foxglove Protobuf

```python
from mcap_protobuf.writer import Writer

Writer.write_message(
    topic: str,
    message: Any,
    log_time: int | None = None,
    publish_time: int | None = None,
    sequence: int = 0)[source]
```

Writes a message to an MCAP file.

Parameters:
- **topic:** the topic that this message was originally published on.
- **message:** a Protobuf object to write into the MCAP.
- **log_time:** unix nanosecond timestamp of when this message was written to the MCAP.
- **publish_time:** unix nanosecond timestamp of when this message was originally published.
- **sequence:** an optional sequence count for messages on this topic.


- [schemas](https://github.com/foxglove/schemas/tree/main/schemas/proto/foxglove)
    - CameraCalibration
    - CompressedImage
    - CompressedVideo
    - FrameTransform[s]
    - GeoJSON
    - LaserScan
    - LocationFix
    - Log
    - Pose[InFrame[s]]
    - Quaternion
    - RawImage
    - Vector3
    - more ...

```protobuf
syntax = "proto3";

import "google/protobuf/timestamp.proto";

package foxglove;

// A raw image
message RawImage {
  // Timestamp of image
  google.protobuf.Timestamp timestamp = 1;

  // Frame of reference for the image. The origin of the frame
  // is the optical center of the camera. +x points to the right
  // in the image, +y points down, and +z points into the plane
  // of the image.
  string frame_id = 7;

  // Image width
  fixed32 width = 2;

  // Image height
  fixed32 height = 3;

  // Encoding of the raw image data
  //
  // Supported values: `8UC1`, `8UC3`, `16UC1` (little endian),
  // `32FC1` (little endian), `bayer_bggr8`, `bayer_gbrg8`,
  // `bayer_grbg8`, `bayer_rggb8`, `bgr8`, `bgra8`, `mono8`,
  // `mono16`, `rgb8`, `rgba8`, `uyvy` or `yuv422`, `yuyv` or
  // `yuv422_yuy2`
  string encoding = 4;

  // Byte length of a single row
  fixed32 step = 5;

  // Raw image data
  bytes data = 6;
}
```

```protobuf
syntax = "proto3";

import "google/protobuf/timestamp.proto";

package foxglove;

// A compressed image
message CompressedImage {
  // Timestamp of image
  google.protobuf.Timestamp timestamp = 1;

  // Frame of reference for the image. The origin of the frame is the
  // optical center of the camera. +x points to the right in the image,
  // +y points down, and +z points into the plane of the image.
  string frame_id = 4;

  // Compressed image data
  bytes data = 2;

  // Image format
  //
  // Supported values: image media types supported by Chrome, such as
  // `webp`, `jpeg`, `png`
  string format = 3;
}
```

```protobuf
syntax = "proto3";

import "foxglove/Pose.proto";
import "google/protobuf/timestamp.proto";

package foxglove;

// A single scan from a planar laser range-finder
message LaserScan {
  // Timestamp of scan
  google.protobuf.Timestamp timestamp = 1;

  // Frame of reference
  string frame_id = 2;

  // Origin of scan relative to frame of reference; points are positioned
  // in the x-y plane relative to this origin; angles are interpreted as
  // counterclockwise rotations around the z axis with 0 rad being in the +x
  // direction
  foxglove.Pose pose = 3;

  // Bearing of first point, in radians
  double start_angle = 4;

  // Bearing of last point, in radians
  double end_angle = 5;

  // Distance of detections from origin; assumed to be at equally-spaced angles
  // between `start_angle` and `end_angle`
  repeated double ranges = 6;

  // Intensity of detections
  repeated double intensities = 7;
}
```

# MIT License

**Copyright (c) 2024 Mom's Friendly Robot Company**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
