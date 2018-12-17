#!/usr/bin/env bash

if [[ -z "$1" ]]; then
    echo "Kindly specify a directory, Thanks :-)"
    exit
else
    cd $1
fi

rm -rf dist build */*.egg-info *.egg-info

python setup.py sdist bdist_wheel

twine upload -r internal dist/*
