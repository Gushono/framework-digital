import connexion
from flask_cors import CORS

from server.configurations.filters import before_request
from server.configurations.logger import create_logger
from server.models.exceptions import (
    NotFound,
    Unauthorized,
    generic_render,
    ApiBaseException
)

logger = create_logger()


def initiate_server():
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.add_api("swagger.yaml", pythonic_params=True)

    app.add_error_handler(ApiBaseException, generic_render)
    app.add_error_handler(NotFound, generic_render)
    app.add_error_handler(Unauthorized, generic_render)

    CORS(app.app)
    app.app.before_request(before_request)

    return app
