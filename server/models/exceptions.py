import json

from flask import Response


class ApiBaseException(Exception):
    status_code = 500
    message = None
    payload = None
    detail = None

    def __init__(self, message, detail=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload
        self.detail = detail


def generic_render(exception: ApiBaseException):
    return Response(
        response=json.dumps(
            {"error": {"reason": exception.message}}
        ),
        status=exception.status_code,
        mimetype="application/json",
    )


class Unauthorized(ApiBaseException):
    status_code = 401
    message = "Not authorized! Token invalid or not found"

    def __init__(self, message=None, payload=None):
        self.message = message if message is not None else self.message
        ApiBaseException.__init__(self, self.message, payload)


class NotFound(ApiBaseException):
    status_code = 404
    message = "Entity not found"

    def __init__(self, message=None, payload=None):
        self.message = message if message is not None else self.message
        ApiBaseException.__init__(self, self.message, payload)