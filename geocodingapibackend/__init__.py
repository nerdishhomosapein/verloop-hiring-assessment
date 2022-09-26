from flasgger import Swagger
from flask import Flask

from geocodingapibackend.routes.error import error_bp


def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)  # noqa: F841

    app.register_blueprint(error_bp)
    return app
