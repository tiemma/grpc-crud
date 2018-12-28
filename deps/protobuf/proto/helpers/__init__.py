from datetime import datetime
from os.path import abspath, split, join
from os import getenv

from grpc import ssl_channel_credentials, secure_channel, ssl_server_credentials

default_port = '50051'
default_host_name = 'localhost'


def create_timestamp():
    """

    :return:
    """
    return datetime.now().isoformat()


def get_cert_path():
    """

    :return:
    """
    return abspath(split(__file__)[0] + getenv("GRPC_CERT_PATH", "/../cert"))


def get_encoded_cert():
    """

    :return:
    """
    # read in certificate
    with open(join(get_cert_path(), getenv("GRPC_CERT_NAME", 'server.crt'))) as f:
        return f.read().encode()


def get_encoded_cert_key():
    """

    :return:
    """
    with open(join(get_cert_path(), getenv("GRPC_KEY_NAME",'server.key'))) as f:
        return f.read().encode()


def create_channel():
    """

    :return:
    """
    # Create credentials
    credentials = ssl_channel_credentials(root_certificates=get_encoded_cert())
    return secure_channel(
        '{HOST}:{PORT}'.format(HOST=getenv('GRPC_HOST_NAME', default_host_name), PORT=getenv('GRPC_PORT', default_port)),
        credentials)

