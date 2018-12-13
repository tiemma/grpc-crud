from bcrypt import hashpw, gensalt
from concurrent import futures
from os.path import join, split, abspath
from os import getenv
from time import sleep
from uuid import uuid1, uuid4

from grpc import server as grpc_server, ssl_server_credentials

from src.grpc.helpers import create_timestamp
from src.grpc.proto.User_pb2_grpc import CreateUserServiceServicer, add_CreateUserServiceServicer_to_server
from src.grpc.proto.User_pb2 import User, UserResponse
from src.grpc.proto.Helpers_pb2 import Timestamp, UUID, UserStatus


class UserService(CreateUserServiceServicer):

    def CreateUser(self, request, context):
        encr_password = hashpw(request.password.encode(), gensalt())
        user = User(name=request.name,
                    email=request.email,
                    password=encr_password)
        created_at = Timestamp(timeStamp=create_timestamp())
        updated_at = Timestamp(timeStamp=create_timestamp())
        user_id = UUID(id=str(uuid1()))
        user_status = UserStatus.Value(UserStatus.Name(0))
        is_verified = False
        token = str(uuid4())
        return UserResponse(user=user,
                            userStatus=user_status,
                            userId=user_id,
                            token=token,
                            createdAt=created_at,
                            updatedAt=updated_at,
                            isVerified=is_verified)


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

    server.add_secure_port(
        '{HOST}:{PORT}'.format(HOST=getenv('HOST', 'localhost'), PORT=getenv('PORT', 50051)),
        server_creds)

    server.start()

    print("Server started successfully")

    try:
        while True:
            sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()