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

from __future__ import print_function
import logging

import sys
from time import sleep
import signal
import threading

import grpc

import deepthought_pb2
import deepthought_pb2_grpc

def run():
    # !! do NOT use insecure_channel for production !!
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = deepthought_pb2_grpc.ComputeStub(channel)
        # stub.<rpc>(*_pb2.<message>(param))
        #for response in stub.Boot(deepthought_pb2.BootRequest()):
        #    print(">>> BootRequest Sent. response: %s" % (response.message))
        response_generator = stub.Boot(deepthought_pb2.BootRequest())
        
        def cancel_request():
            response_generator.cancel()
            sys.exit(0)
        # send cancel and exit(0) when receiving SIGINT (e.g. Ctrl+C)
        def cancel_request_sigint(unused_signum, unused_frame):
            cancel_request()
        signal.signal(signal.SIGINT, cancel_request_sigint)
        # send cancel after 1.5 seconds
        threading.Timer(1.5, cancel_request).start()

        # receive message from server
        try:
            for response in response_generator:
                print(">>> BootRequest Sent. response: %s" % (response.message))
        except grpc.RpcError as e:
            print(">>> Cancelled: Boot Server-side Streaming")
            #print(e)
        
        # class grpc.UnaryUnaryMultiCallable
        response = stub.Infer(deepthought_pb2.InferRequest(query='Infer Query'))
        response = stub.Infer(deepthought_pb2.InferRequest(query='Infer Query'), timeout=300)
        print(">>> type(response): " + str(type(response)))
        print(">>> InferRequest Sent. response: %s, %s" % (response.answer, response.description))
    

if __name__ == '__main__':
    logging.basicConfig()
    run()
