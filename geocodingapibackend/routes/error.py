from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound

error_bp = Blueprint("errors", __name__)


@error_bp.app_errorhandler(NotFound)
def handle_not_found(err):
    return jsonify({"message": "Resource not found"}), 404


@error_bp.app_errorhandler(Exception)
def handle_generic_exception(err):
    return jsonify({"message": "Unknown Error. Check logs for more details."}), 500
