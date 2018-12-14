from bcrypt import hashpw, gensalt

from time import sleep
from uuid import uuid1, uuid4


from proto.helpers import create_timestamp, create_user_service
from proto.User_pb2_grpc import CreateUserServiceServicer
from proto.User_pb2 import User, UserResponse
from proto.Helpers_pb2 import Timestamp, UUID, UserStatus


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

    # Sleep time in seconds
    one_day_in_seconds = 60 * 60 * 24

    server = create_user_service(UserService())

    server.start()

    print("Server started successfully")

    try:
        while True:
            sleep(one_day_in_seconds)
    except KeyboardInterrupt:
        server.stop(0)
