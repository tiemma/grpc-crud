#!/usr/bin/env bash

exportProtobuf () {

    DESTDIR=$(pwd)/../deps/protobuf_deps/;
    mkdir -p $DESTDIR;

    #Extra proto directory was added so that it generates the right package import after compilation
    # from proto import <PROTO_CLASS>
    PROTO_FILE=$(pwd)/proto/*.proto

    echo $PROTO_FILE;

    python -m grpc_tools.protoc \
        --proto_path=$(pwd)/\
        --python_out=$DESTDIR \
        --plugin=protoc-gen-grpc_python=`which grpc_python_plugin` \
        --grpc_python_out=$DESTDIR \
        $PROTO_FILE;

}

if [[ -z "$1" ]]; then
    echo "Kindly specify a command here, Thanks :-)"
else
    "$@"
fi

