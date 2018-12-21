from os import getenv

from bcrypt import hashpw, gensalt

from time import sleep
from uuid import uuid1, uuid4

from logger import Logger

from proto.helpers import create_timestamp, create_user_service, default_port
from proto.User_pb2_grpc import CreateUserServiceServicer
from proto.User_pb2 import User, UserResponse
from proto.Helpers_pb2 import Timestamp, UUID, USER


class UserService(CreateUserServiceServicer):
    """

    """

    logger = Logger.get_logger(__name__)

    def CreateUser(self, request, context):
        """

        :param request:
        :param context:
        :return:
        """
        self.logger.debug('Creating user response object')
        encr_password = hashpw(request.password.encode(), gensalt())
        user = User(name=request.name,
                    email=request.email,
                    password=encr_password)
        created_at = Timestamp(time_stamp=create_timestamp())
        updated_at = Timestamp(time_stamp=create_timestamp())
        user_id = UUID(id=str(uuid1()))
        user_status = USER
        is_verified = False
        token = str(uuid4())
        self.logger.debug('User response object successfully created')
        return UserResponse(user=user,
                            user_status=user_status,
                            user_id=user_id,
                            token=token,
                            created_at=created_at,
                            updated_at=updated_at,
                            is_verified=is_verified)


def serve():
    """

    """
    # Sleep time in seconds
    one_day_in_seconds = 60 * 60 * 24

    server = create_user_service(UserService())

    server.start()

    Logger.get_logger(__name__).debug("Server started successfully on port {}".format(getenv('PORT', default_port)))

    try:
        while True:
            sleep(one_day_in_seconds)
    except KeyboardInterrupt:
        server.stop(0)
