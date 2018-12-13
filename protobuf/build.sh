#!/usr/bin/env bash

exportProtobuf () {

    DESTDIR=$(pwd)/../src/proto;
    mkdir -p $DESTDIR;

    PROTO_FILE=$(pwd)/*.proto
    echo $PROTO_FILE;

    python -m grpc_tools.protoc \
        --proto_path=$(pwd)\
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

