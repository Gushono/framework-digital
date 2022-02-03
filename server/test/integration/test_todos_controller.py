from server.test.integration import BaseTestCase
from server.test.integration.mocks import INVALID_ASSIGNATURE_TOKEN, EXPIRED_TOKEN


def get(self, url: str, headers: dict, params=None):
    """
    Get method used to api todos
    """

    if params is None:
        params = {}

    return self.client.open(
        self.base_url(url),
        method="GET",
        headers=headers,
        query_string=params
    )


def post(self, url: str, username: str or None, password: str or None):
    """
    Post method used to auth
    """

    return self.client.open(
        self.base_url(url),
        method="POST",
        auth=(username, password)
    )


class TestTodosController(BaseTestCase):
    """
    """
    url = "todos"

    def test_list_todos_with_valid_token(self):
        correct_user, correct_pass = 'ADMIN', 'SecretPass'

        response_token = post(self, 'auth', username=correct_user, password=correct_pass)
        response_token_json = response_token.json

        headers = {"x-api-key": response_token_json['x-api-key']}

        response_todos = get(self, self.url, headers=headers)
        response_todos_json = response_todos.json

        self.assertEqual(response_todos.status_code, 200)
        self.assertEqual(len(response_todos_json), 200)
        self.assertEqual(response_todos_json[0]['id'], 1)

    def test_list_todos_with_invalid_assignature_token(self):
        headers = {"x-api-key": INVALID_ASSIGNATURE_TOKEN}

        response_todos = get(self, self.url, headers=headers)
        response_todos_json = response_todos.json

        self.assertEqual(response_todos_json['error']['reason'], 'Signature verification failed!')
        self.assertEqual(response_todos.status_code, 401)

    def test_list_todos_with_expired_token(self):
        headers = {"x-api-key": EXPIRED_TOKEN}

        response_todos = get(self, self.url, headers=headers)
        response_todos_json = response_todos.json

        self.assertEqual(response_todos_json['error']['reason'], 'Token is expired. Please, generate another!')
        self.assertEqual(response_todos.status_code, 401)

    def test_list_todos_with_query_params(self):
        correct_user, correct_pass = 'ADMIN', 'SecretPass'

        response_token = post(self, 'auth', username=correct_user, password=correct_pass)
        response_token_json = response_token.json

        headers = {"x-api-key": response_token_json['x-api-key']}

        response_todos = get(self, self.url, headers=headers, params={'userId': 1})
        response_todos_json = response_todos.json

        self.assertEqual(response_todos.status_code, 200)
        self.assertEqual(len(response_todos_json), 20)
        self.assertEqual(response_todos_json[0]['id'], 1)

    def test_todos_by_id(self):
        correct_user, correct_pass = 'ADMIN', 'SecretPass'

        response_token = post(self, 'auth', username=correct_user, password=correct_pass)
        response_token_json = response_token.json

        headers = {"x-api-key": response_token_json['x-api-key']}

        response_todos = get(self, self.url + '/1', headers=headers)
        response_todos_json = response_todos.json

        self.assertEqual(response_todos.status_code, 200)
        self.assertEqual(response_todos_json['id'], 1)
        self.assertEqual(response_todos_json['title'], 'delectus aut autem')
