
from flask import Blueprint
from flask_pydantic import validate


auth_bp = Blueprint("Authentication",__name__)


@auth_bp.route("/register", methods=["POST"])
@validate()
def register():
    return {"msg": "test"}

@auth_bp.route("/login", methods=["POST"])
@validate()
def login():
    return "login"

@auth_bp.route("/refresh")
def refresh_token():
    return "token refresh"

@auth_bp.route("/update", methods=["PUT"])
def update_user():
    return "user update"

@auth_bp.route("/logout", methods=["DELETE"])
def logout():
    return "logout"

