FROM python:3.5-alpine

ENV HOST 0.0.0.0

ENV PORT 50010

RUN pwd

RUN pip3 install pipenv

ADD __init__.py Pipfile server.py app/

ADD ../../deps/protobuf-deps/proto/cert  /cert

ADD helpers/ app/helpers

ADD ../../deps/protobuf-deps/proto app/proto

ADD server/ app/server/

WORKDIR app/

RUN pipenv install --skip-lock

RUN pwd

RUN ls

CMD ["pipenv", "run", "python3", "server.py"]