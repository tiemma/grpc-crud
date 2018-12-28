from os import getenv


from bcrypt import hashpw, gensalt
from concurrent import futures
from grpc import server as grpc_server, ssl_server_credentials

from time import sleep
from uuid import uuid1, uuid4

from logger import Logger

from proto.helpers import create_timestamp, default_port, default_host_name, get_encoded_cert_key, get_encoded_cert
from proto.User_pb2_grpc import CreateUserServiceServicer, add_CreateUserServiceServicer_to_server
from proto.User_pb2 import User, UserResponse
from proto.Helpers_pb2 import Timestamp, UUID, USER


class UserService(CreateUserServiceServicer):
    """

    """

    logger = Logger.get_logger(__name__)

    def CreateUser(self, request, context):
        """
        CreateUser class overrides one in CreateUserServiceServicer which will throw a
        NotImplementedError hence the reason for leaving it capitalized and now following
        format highlighted in other functions below, for example

        :param request:
        :param context:
        :return:
        """
        self.logger.debug('Creating user response object with request %r and context %r', request, context)
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


def create_user_service(server, user_service):
    """

    :param server: GRPC Server Instance
    :param user_service: Instance of the rpc service defined in the protobuf struct
    :return:
    """
    add_CreateUserServiceServicer_to_server(user_service, server)
    server_creds = ssl_server_credentials(((get_encoded_cert_key(), get_encoded_cert(),),))
    server.add_secure_port(
        '{HOST}:{PORT}'.format(HOST=getenv('GRPC_HOST_NAME', default_host_name), PORT=getenv('GRPC_PORT', default_port)),
        server_creds)

    return server


def serve():
    """

    """
    # Sleep time in seconds
    one_day_in_seconds = 60 * 60 * 24

    server = grpc_server(futures.ThreadPoolExecutor(max_workers=int(getenv('GRPC_MAX_WORKERS', '10'))))

    create_user_service(server, UserService())

    server.start()

    Logger.get_logger(__name__).debug("Server started successfully on port {}".format(getenv('GRPC_PORT', default_port)))

    try:
        while True:
            sleep(one_day_in_seconds)
    except KeyboardInterrupt:
        server.stop(0)
