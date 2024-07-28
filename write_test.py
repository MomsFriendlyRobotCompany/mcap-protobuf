#!/usr/bin/env python3
# write_message(
#     topic: str,
#     message: Any,
#     log_time: int | None = None,
#     publish_time: int | None = None,
#     sequence: int = 0)[source]
# Writes a message to an MCAP file.
#
# Parameters:
#     topic: the topic that this message was originally published on.
#     message: a Protobuf object to write into the MCAP.
#     log_time: unix nanosecond timestamp of when this message was written to the MCAP.
#     publish_time: unix nanosecond timestamp of when this message was originally published.
#     sequence: an optional sequence count for messages on this topic.

import sys
from time import sleep, time_ns
import datetime as dt
from mcap_protobuf.writer import Writer
from py.msgs_pb2 import Imu, Vector, Quaternion


def main():
    with open(sys.argv[1], "wb") as f, Writer(f) as mcap_writer:
        for i in range(10):
            ts = time_ns()
            mcap_writer.write_message(
                topic="/simple_messages",
                message=Imu(
                    accels=Vector(x=1*i,y=-2*i,z=3),
                    gyros=Vector(x=1,y=2,z=3),
                    mags=Vector(x=1,y=2,z=3),
                    temperature=20.333,
                    altitude=100+i,
                    pressure=1010.111,
                    orientation=Quaternion(w=1,x=0,y=0,z=0),
                    timestamp=ts,
                ),
                log_time=ts,
                publish_time=ts,
            )

            sleep(0.25)


if __name__ == "__main__":
    main()