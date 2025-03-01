
from base64 import b64encode

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

def make_protobuf_channel(topic, class_type):
  info = {
    "topic": topic,
    "encoding": "protobuf",
    "schemaName": class_type.DESCRIPTOR.full_name,
    "schema": b64encode(
        build_file_descriptor_set(class_type).SerializeToString()
    ).decode("ascii"),
    "schemaEncoding": "protobuf",
  }
  return info