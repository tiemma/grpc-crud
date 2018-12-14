
from os import urandom


class Config:
    """
    Config base class
    """
    DEBUG = True
    SECRET_KEY = urandom(256)
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = urandom(256)
    RESTPLUS_VALIDATE = True


class Development(Config):
    pass


class Testing(Config):
    pass


class Production(Config):
    pass


CONFIG_BY_NAME = dict(
    development=Development,
    production=Production,
    testing=Testing
)

if __name__ == "__main__":
    print(Config)