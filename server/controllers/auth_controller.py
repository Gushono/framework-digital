from server.services import auth_service


def post_auth():
    """
    POST -> /auth

    Auth the user and return a token.

    :return: AuthResultSchema in swagger
    """
    return auth_service.post_auth()
