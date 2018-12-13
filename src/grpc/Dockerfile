FROM python3:alpine

ENV HOST 0.0.0.0

ENV PORT 50010

ADD cert helpers proto server __init__.py app/

WORKDIR app/

RUN pip3 install pipenv

RUN pipenv install

CMD ["pipenv", "run", "python3", "server/user/UserService.py"]