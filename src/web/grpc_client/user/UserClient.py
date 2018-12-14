from os import getenv
from os.path import abspath, split, join
from sys import exit

from grpc import ssl_channel_credentials, secure_channel, channel_ready_future, FutureTimeoutError, RpcError

from helpers import get_cert_path
from proto.User_pb2_grpc import CreateUserServiceStub
from proto.User_pb2 import User


def run():

    # Path where certificate and key are defined
    cert_path = get_cert_path()

    # read in certificate
    with open(join(cert_path, 'server.crt')) as f:
        trusted_certs = f.read().encode()

    # create credentials
    credentials = ssl_channel_credentials(root_certificates=trusted_certs)
    channel = secure_channel(
        '{HOST}:{PORT}'.format(HOST=getenv('HOST', 'localhost'), PORT=getenv('PORT', 50051)),
        credentials)
    try:
        channel_ready_future(channel).result(timeout=getenv('TIMEOUT', 10))
    except FutureTimeoutError:
        exit('Error connecting to server')
    else:
        stub = CreateUserServiceStub(channel)
        metadata = [('ip', getenv('HOST', 'localhost'))]

        try:
            response = stub.CreateUser(
                User(name="Bakare Emmanuel", email="blank@gmail.com", password="2312"),
                metadata=metadata,
            )
        except RpcError as e:
            print('CreateUser failed with {0}: {1}'.format(e.code(), e.details()))
        else:
            print("User created: \n", response)


if __name__ == '__main__':
    run()