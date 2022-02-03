import logging

from flask_testing import TestCase

from server import initiate_server


class BaseTestCase(TestCase):

    @staticmethod
    def create_app(**kwargs):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = initiate_server()
        return app.app

    @staticmethod
    def base_url(url):
        return f"/v1/{url}"
