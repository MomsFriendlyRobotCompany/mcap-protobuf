from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Vector(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Quaternion(_message.Message):
    __slots__ = ("w", "x", "y", "z")
    W_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    w: float
    x: float
    y: float
    z: float
    def __init__(self, w: _Optional[float] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

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
    accels: Vector
    gyros: Vector
    mags: Vector
    orientation: Quaternion
    imu_temp: float
    temperature: float
    pressure: float
    altitude: float
    calibrated: bool
    timestamp: int
    def __init__(self, accels: _Optional[_Union[Vector, _Mapping]] = ..., gyros: _Optional[_Union[Vector, _Mapping]] = ..., mags: _Optional[_Union[Vector, _Mapping]] = ..., orientation: _Optional[_Union[Quaternion, _Mapping]] = ..., imu_temp: _Optional[float] = ..., temperature: _Optional[float] = ..., pressure: _Optional[float] = ..., altitude: _Optional[float] = ..., calibrated: bool = ..., timestamp: _Optional[int] = ...) -> None: ...
