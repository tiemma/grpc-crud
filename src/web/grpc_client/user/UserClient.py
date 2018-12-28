from os import getenv
from sys import exit
from typing import Dict

from grpc import channel_ready_future, FutureTimeoutError, RpcError
from google.protobuf.json_format import MessageToDict

from logger import Logger

from proto.helpers import create_channel
from proto.User_pb2_grpc import CreateUserServiceStub
from proto.User_pb2 import User


def create_user(request: Dict):
    channel = create_channel()
    log = Logger.get_logger(__name__)

    try:
        channel_ready_future(channel).result(timeout=getenv('TIMEOUT', 10))
    except FutureTimeoutError:
        exit('Error connecting to server')
    else:
        stub = CreateUserServiceStub(channel)
        metadata = [('ip', getenv('HOST', 'localhost'))]

        try:
            response = stub.CreateUser(
                User(name=request['name'], email=request['email'], password=request['password']),
                metadata=metadata,
            )
        except RpcError as e:
            log.debug('CreateUser failed with %r: %r', e.code(), e.details())
        else:
            return MessageToDict(response, including_default_value_fields=True)

