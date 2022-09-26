from flask import Flask
from flasgger import Swagger

from geocodingapibackend.routes.error import error_bp


def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)

    app.register_blueprint(error_bp)
    return app
