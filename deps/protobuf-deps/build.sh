#!/usr/bin/env bash

rm -rf dist build */*.egg-info *.egg-info

python setup.py sdist bdist_wheel

twine upload -r internal dist/*
