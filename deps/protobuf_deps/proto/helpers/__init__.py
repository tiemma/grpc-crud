from datetime import datetime
from os.path import abspath, split, join
from os import getenv
from concurrent import futures

from proto.User_pb2_grpc import add_CreateUserServiceServicer_to_server

from grpc import ssl_channel_credentials, secure_channel, server as grpc_server, ssl_server_credentials

default_port = '50051'


def create_timestamp():
    """

    :return:
    """
    return datetime.now().isoformat()


def get_cert_path():
    """

    :return:
    """
    return abspath(split(__file__)[0] + "/../cert")


def get_encoded_cert():
    """

    :return:
    """
    # read in certificate
    with open(join(get_cert_path(), 'server.crt')) as f:
        return f.read().encode()


def get_encoded_cert_key():
    """

    :return:
    """
    with open(join(get_cert_path(), 'server.key')) as f:
        return f.read().encode()


def create_channel():
    """

    :return:
    """
    # Create credentials
    credentials = ssl_channel_credentials(root_certificates=get_encoded_cert())
    return secure_channel(
        '{HOST}:{PORT}'.format(HOST=getenv('HOST', 'localhost'), PORT=getenv('PORT', default_port)),
        credentials)


def create_user_service(user_service):
    """

    :param user_service:
    :return:
    """
    server = grpc_server(futures.ThreadPoolExecutor(max_workers=10))
    add_CreateUserServiceServicer_to_server(user_service, server)

    server_creds = ssl_server_credentials(((get_encoded_cert_key(), get_encoded_cert(),),))
    server.add_secure_port(
        '{HOST}:{PORT}'.format(HOST=getenv('HOST', 'localhost'), PORT=getenv('PORT', default_port)),
        server_creds)

    return server
