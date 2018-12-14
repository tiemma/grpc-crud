"""
Entry module for starting the grpc server

"""
from server.user.UserService import serve

if __name__ == "__main__":
    serve()
