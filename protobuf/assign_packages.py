
from subprocess import call
from os import getcwd, listdir


proto_directory = '{}/../deps/protobuf_deps/proto'.format(getcwd())


def get_proto_files():
    proto_files = [i for i in listdir(proto_directory) if "_pb2" in i]

    print(proto_files)

    return proto_files


def add_package_to_import(package_ext):
    for file in get_proto_files():
        for proto_module in ['Comment_pb2', 'Helpers_pb2', 'User_pb2']:
            call(["sed -i -e 's/{proto_module}/{package_ext}.{proto_module}/' '{proto_directory}/{file}'".format(proto_module=proto_module,
                                                                                                         package_ext=package_ext,
                                                                                                         proto_directory=proto_directory,
                                                                                                         file=file)],
                 shell=True)


if __name__ == "__main__":
    add_package_to_import('proto')