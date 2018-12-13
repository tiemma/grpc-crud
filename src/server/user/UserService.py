
from concurrent import futures
from grpc import server as grpc_server, ssl_server_credentials
from os.path import join, split, abspath
from time import sleep

from src.proto.User_pb2_grpc import CreateUserServiceServicer, add_CreateUserServiceServicer_to_server
from src.proto.User_pb2 import User, UserResponse

class UserService(CreateUserServiceServicer):

    def CreateUser(self, request, context):
        user = User(name=request.name, email=request.email, password=request.password)
        return UserResponse(user=user)


def serve():
    server = grpc_server(futures.ThreadPoolExecutor(max_workers=10))
    add_CreateUserServiceServicer_to_server(UserService(), server)

    # Path where certificate and key are defined
    cert_path = abspath(split(__file__)[0] + "/../../cert")

    # Sleep time in seconds
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24

    with open(join(cert_path, 'server.key')) as f:
        private_key = f.read().encode()

    with open(join(cert_path, 'server.crt')) as f:
        certificate_chain = f.read().encode()

    server_creds = ssl_server_credentials(((private_key, certificate_chain,),))

    server.add_secure_port('localhost:50051', server_creds)

    server.start()

    print("Server started successfully")

    try:
        while True:
            sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()