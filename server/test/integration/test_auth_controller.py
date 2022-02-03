from datetime import datetime

from server.configurations.filters import decode_token
from server.test.integration import BaseTestCase


def post(self, url: str, username: str or None, password: str or None):
    """
    Post method used to auth
    """

    return self.client.open(
        self.base_url(url),
        method="POST",
        auth=(username, password)
    )


def options(self, url: str):
    """
    Options to check cors
    """

    return self.client.open(
        self.base_url(url),
        method="OPTIONS",
    )


class TestAuthController(BaseTestCase):
    """
    """
    url = "auth"

    def test_auth_with_right_users(self):
        correct_user, correct_pass = 'ADMIN', 'SecretPass'

        response = post(self, self.url, username=correct_user, password=correct_pass)
        response_json = response.json

        token_info = decode_token(response_json['x-api-key'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(token_info), 2)

    def test_generated_token_is_not_expired(self):
        correct_user, correct_pass = 'ADMIN', 'SecretPass'

        response = post(self, self.url, username=correct_user, password=correct_pass)
        response_json = response.json

        token_info = decode_token(response_json['x-api-key'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(token_info), 2)
        self.assertTrue(datetime.fromisoformat(token_info['expiration_date']) > datetime.now())

    def test_auth_with_wrong_user_and_correct_pass(self):
        wrong_user, correct_pass = 'WRONG', 'SecretPass'

        response = post(self, self.url, username=wrong_user, password=correct_pass)

        self.assertEqual(response.status_code, 401)

    def test_auth_with_correct_user_and_wrong_pass(self):
        correct_user, wrong_pass = 'ADMIN', 'WRONG'

        response = post(self, self.url, username=correct_user, password=wrong_pass)

        self.assertEqual(response.status_code, 401)

    def test_auth_with_wrong_user_and_wrong_pass(self):
        wrong_user, wrong_pass = 'WRONG', 'WRONG'

        response = post(self, self.url, username=wrong_user, password=wrong_pass)

        self.assertEqual(response.status_code, 401)

    def test_auth_with_no_user_and_no_pass(self):
        response = post(self, self.url, username=None, password=None)

        self.assertEqual(response.status_code, 401)

    def test_auth_with_empty_user_and_empty_pass(self):
        response = post(self, self.url, username='', password='')

        self.assertEqual(response.status_code, 401)

    def test_options(self):
        response = options(self, self.url)

        self.assertEqual(response.status_code, 200)
