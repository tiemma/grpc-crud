#!/usr/bin/env bash


# Doing this just incase I change the keys and I need to build and update them
cp -R $(pwd)/../cert $(pwd)/cert

docker build -t grpc-crud:server .