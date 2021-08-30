# Copyright 2021 Kentaro Ebisawa <ebiken.g@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Note:
#   This is tutorial outcome of https://github.com/ymmt2005/grpc-tutorial
#   Below sample code are referenced when working on this.
#   * https://github.com/grpc/grpc/tree/master/examples/python/helloworld

from concurrent import futures
import logging

from time import sleep

import grpc

import deepthought_pb2
import deepthought_pb2_grpc

#from google.rpc import code_pb2, status_pb2
from grpc_status import rpc_status
from google.protobuf import any_pb2


def make_boot_msg(s):
    msg = "Boot " + str(s)
    return deepthought_pb2.BootResponse(message=msg)

# Compute: service name in .proto
class Compute(deepthought_pb2_grpc.ComputeServicer):
    # define rpc handlers
    def Boot(self, request, context):
        for m in range(100):
            yield make_boot_msg(m)
            sleep(0.5)

    def Infer(self, request, context):
        t = context.time_remaining()
        # Hack. `if t is not None:` is always true even if timeout was not specified
        if t > 9000000:
            print("No timeout set")
            t = 0
        if t > 0 and t < 0.75:
            print("Peer %s connected. time_remianing (deadline): %f sec" % (context.peer(), t))
            return deepthought_pb2.InferResponse(answer=9999, description='Hello Infer! request.query: %s!' % request.query)

        # Retern DEADLINE_EXCEEDED (code 4) error if time exeded.
        context.abort_with_status(rpc_status.to_status())
        return status_pb2.Status(
            code=code_pb2.DEADLINE_EXCEEDED,
            message='It would take longer',
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    deepthought_pb2_grpc.add_ComputeServicer_to_server(Compute(), server)
    server.add_insecure_port('[::]:50051')
    print(">> Server: Starting on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
