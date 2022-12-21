import sys
from pathlib import Path
path_root = Path(__file__).parent
sys.path.insert(0, str(path_root))

import os
import grpc
import fib_pb2
import fib_pb2_grpc
import logging
import math


def fib(index):
    if index < 0:
        return math.nan
    elif index == 0 or index == 1:
        return index
    else:
        p0 = 0
        p1 = 1
        for _ in range(2, index+1):
            p2 = p0 + p1
            p0 = p1
            p1 = p2
        return p2


def fib_grpc(host, index):
    channel = grpc.insecure_channel(host)
    stub = fib_pb2_grpc.FibStub(channel)
    request = fib_pb2.FibRequest(index=index)
    print(request)
    reply = stub.Run(request)
    channel.close()
    return reply.value
