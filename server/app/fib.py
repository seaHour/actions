import concurrent.futures
import grpc
import os
import math
import logging
import fib_pb2
import fib_pb2_grpc


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
logger.setLevel(LOG_LEVEL)


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


class FibServicer(fib_pb2_grpc.FibServicer):

    def Run(self, request, context):
        logger.debug(f"receive incoming call with index {request.index}")
        f = fib(request.index)
        return fib_pb2.FibReply(value=f)


def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    fib_pb2_grpc.add_FibServicer_to_server(FibServicer(), server)
    
    server.add_insecure_port('[::]:50051')
    logger.debug("start fib grpc server...")

    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
