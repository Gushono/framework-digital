import datetime

import connexion
import jwt
from flask import jsonify

from server import Unauthorized
from server.configurations.constant import LOGIN_VALID, SECRET_KEY


def post_auth():
    """
    Function that generate a token with the user is valid

    :return: AuthResultSchema in swagger

    :exceptions: Unauthorized if user and password is invalid
    """

    auth: dict or None = connexion.request.authorization if connexion.request.authorization else {}
    username, password = auth.get("username"), auth.get("password")

    if not is_login_valid(username, password):
        raise Unauthorized(message="Username and password invalid! Please, use basic auth!")

    return jsonify({"x-api-key": generate_jwt_token(username=username)})


def is_login_valid(username: str, password: str) -> bool:
    """
    This function checks if the username and password is valid.
    """

    if not username or not password:
        return False

    return True if LOGIN_VALID.get(username) == password else False


def generate_jwt_token(username: str) -> str:
    """
    This function generate a jwt token based in the username and the expiration_date.
    """
    expiration_date = datetime.datetime.now() + datetime.timedelta(minutes=30)

    token: str = jwt.encode({
        "username": username,
        "expiration_date": str(expiration_date)
    }, SECRET_KEY)

    return token
