#!/usr/bin/env bash

if [[ -z "$1" ]]; then
    echo "Kindly specify a directory, Thanks :-)"
    exit
else
    cd $1
fi

# Configure authentication for the pypi server, if needed!
export TWINE_USERNAME=pypi
export TWINE_PASSWORD=password

rm -rf dist build */*.egg-info *.egg-info

python setup.py sdist bdist_wheel

twine upload --repository-url http://localhost:8080 dist/*
