import re
from datetime import datetime

import connexion
import flask
import jwt
from jwt import InvalidSignatureError

from server.configurations.constant import SECRET_KEY
from server.models.exceptions import Unauthorized


def before_request():
    if connexion.request.method == 'OPTIONS':
        return

    if is_allowed_url_without_auth():
        return

    token_info = check_x_api_key_token_valid()
    flask.g.username = token_info.get("username")


def is_allowed_url_without_auth() -> bool:
    """
    Verify if the requested url is allowed withou the use of a jwt token.
    """
    allowed_urls = [
        "/v1/ui",
        "/v1/ui/",
        "/v1/swagger.json",
        "/v1/ping",
        "/v1/ping/",
        "/v1/auth"
    ]

    for allowed_url in allowed_urls:
        if re.match(allowed_url, connexion.request.path):
            return True

    return False


def check_x_api_key_token_valid() -> dict:
    """
    Validate x_api_key, and verify if is not expired and if is valid

    :return: Dict with infos of the token.
    :exception: Unauthorized -> Case token is expired or invalid.

    """
    x_api_key = connexion.request.headers.get("x-api-key")

    token_info = decode_token(x_api_key)

    if datetime.now() >= datetime.fromisoformat(token_info.get("expiration_date")):
        raise Unauthorized(message="Token is expired. Please, generate another!")

    return token_info


def decode_token(x_api_key: str) -> dict:
    """
    Decode the token using a secret key.
    """

    try:
        token = jwt.decode(x_api_key,
                           SECRET_KEY,
                           algorithms=["HS256"])
    except InvalidSignatureError as ex:
        print(ex)
        raise Unauthorized("Signature verification failed!")

    return token
