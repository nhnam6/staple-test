from flask import Blueprint, jsonify

health = Blueprint("health", __name__)


@health.route("/health")
def health_api():
    return jsonify({"message": "Ok"})
