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


def create_channel():
    # Path where certificate and key are defined
    cert_path = get_cert_path()

    # read in certificate
    with open(join(cert_path, 'server.crt')) as f:
        trusted_certs = f.read().encode()

    # create credentials
    credentials = ssl_channel_credentials(root_certificates=trusted_certs)
    return secure_channel(
        '{HOST}:{PORT}'.format(HOST=getenv('HOST', 'localhost'), PORT=getenv('PORT', default_port)),
        credentials)


def create_user_service(UserService):
    server = grpc_server(futures.ThreadPoolExecutor(max_workers=10))
    add_CreateUserServiceServicer_to_server(UserService, server)

    # Path where certificate and key are defined
    cert_path = get_cert_path()

    with open(join(cert_path, 'server.key')) as f:
        private_key = f.read().encode()

    with open(join(cert_path, 'server.crt')) as f:
        certificate_chain = f.read().encode()

    server_creds = ssl_server_credentials(((private_key, certificate_chain,),))

    server.add_secure_port(
        '{HOST}:{PORT}'.format(HOST=getenv('HOST', 'localhost'), PORT=getenv('PORT', default_port)),
        server_creds)

    return server
