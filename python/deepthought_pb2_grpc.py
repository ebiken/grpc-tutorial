# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import deepthought_pb2 as deepthought__pb2


class ComputeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Boot = channel.unary_stream(
                '/deepthought.Compute/Boot',
                request_serializer=deepthought__pb2.BootRequest.SerializeToString,
                response_deserializer=deepthought__pb2.BootResponse.FromString,
                )
        self.Infer = channel.unary_unary(
                '/deepthought.Compute/Infer',
                request_serializer=deepthought__pb2.InferRequest.SerializeToString,
                response_deserializer=deepthought__pb2.InferResponse.FromString,
                )


class ComputeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Boot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Infer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComputeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Boot': grpc.unary_stream_rpc_method_handler(
                    servicer.Boot,
                    request_deserializer=deepthought__pb2.BootRequest.FromString,
                    response_serializer=deepthought__pb2.BootResponse.SerializeToString,
            ),
            'Infer': grpc.unary_unary_rpc_method_handler(
                    servicer.Infer,
                    request_deserializer=deepthought__pb2.InferRequest.FromString,
                    response_serializer=deepthought__pb2.InferResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'deepthought.Compute', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Compute(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Boot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/deepthought.Compute/Boot',
            deepthought__pb2.BootRequest.SerializeToString,
            deepthought__pb2.BootResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Infer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/deepthought.Compute/Infer',
            deepthought__pb2.InferRequest.SerializeToString,
            deepthought__pb2.InferResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)