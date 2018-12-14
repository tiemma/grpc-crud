
from flask import Flask
from os import environ


from config import CONFIG_BY_NAME
from server import api

app = Flask(__name__)


def create_app():
    """
    :return:
    """

    print("App initialized")

    app.config.from_object(CONFIG_BY_NAME[environ.get("FLASK_ENV")])

    api.init_app(app)

    return app


@app.before_first_request
def init_db():
    """
    :return:
    """
    pass


if __name__ == "__main__":
    create_app().run()
