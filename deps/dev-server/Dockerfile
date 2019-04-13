FROM python:3.5.7-alpine

WORKDIR /pypi

ARG PIP_USERNAME=pypi

ARG PIP_PASSWORD=password

ARG PYPI_PORT=8080

ADD . /pypi

RUN pip install pipenv

RUN pipenv install pypiserver passlib

RUN mkdir packages

RUN apk update && \
    apk add apache2-utils && \
    htpasswd -b  -sc .htaccess $PIP_USERNAME $PIP_PASSWORD && \
    apk del apache2-utils

ENTRYPOINT [ "pipenv", "run", "pypi-server", "-o", "-vvv", "-P", ".htaccess", "-p", "$PYPI_PORT", "packages" ]

EXPOSE 8080