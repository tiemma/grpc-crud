from os.path import abspath, split, join
from sys import exit

from grpc import ssl_channel_credentials, secure_channel, channel_ready_future, FutureTimeoutError, RpcError
from src.proto.User_pb2_grpc import CreateUserServiceStub
from src.proto.User_pb2 import User

def run():

    # Path where certificate and key are defined
    cert_path = abspath(split(__file__)[0] + "/../../cert")

    # read in certificate
    with open(join(cert_path, 'server.crt')) as f:
        trusted_certs = f.read().encode()

    # create credentials
    credentials = ssl_channel_credentials(root_certificates=trusted_certs)
    channel = secure_channel('localhost:50051', credentials)
    try:
        channel_ready_future(channel).result(timeout=10)
    except FutureTimeoutError:
        exit('Error connecting to server')
    else:
        stub = CreateUserServiceStub(channel)
        metadata = [('ip', '127.0.0.1')]

        try:
            response = stub.CreateUser(
                User(name="Bakare", email="Blank", password="2312"),
                metadata=metadata,
            )
        except RpcError as e:
            print('CreateUser failed with {0}: {1}'.format(e.code(), e.details()))
        else:
            print("User created:", response.user.name)


if __name__ == '__main__':
    run()