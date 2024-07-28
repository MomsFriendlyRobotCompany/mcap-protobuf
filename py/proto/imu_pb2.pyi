from proto import vector_pb2 as _vector_pb2
from proto import quaternion_pb2 as _quaternion_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Imu(_message.Message):
    __slots__ = ("accels", "gyros", "mags", "orientation", "imu_temp", "temperature", "pressure", "altitude", "calibrated", "timestamp")
    ACCELS_FIELD_NUMBER: _ClassVar[int]
    GYROS_FIELD_NUMBER: _ClassVar[int]
    MAGS_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    IMU_TEMP_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    CALIBRATED_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    accels: _vector_pb2.Vector
    gyros: _vector_pb2.Vector
    mags: _vector_pb2.Vector
    orientation: _quaternion_pb2.Quaternion
    imu_temp: float
    temperature: float
    pressure: float
    altitude: float
    calibrated: bool
    timestamp: int
    def __init__(self, accels: _Optional[_Union[_vector_pb2.Vector, _Mapping]] = ..., gyros: _Optional[_Union[_vector_pb2.Vector, _Mapping]] = ..., mags: _Optional[_Union[_vector_pb2.Vector, _Mapping]] = ..., orientation: _Optional[_Union[_quaternion_pb2.Quaternion, _Mapping]] = ..., imu_temp: _Optional[float] = ..., temperature: _Optional[float] = ..., pressure: _Optional[float] = ..., altitude: _Optional[float] = ..., calibrated: bool = ..., timestamp: _Optional[int] = ...) -> None: ...
