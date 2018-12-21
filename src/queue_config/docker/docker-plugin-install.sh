#!/bin/bash

PLUGIN_PATH="/usr/share/elasticsearch/plugins/$1"

if [ ! -d "$PLUGIN_PATH" ]; then
    plugin install $1
fi


if [ -d "$PLUGIN_PATH" ]; then
    echo "$1 plugin already installed"
fi

