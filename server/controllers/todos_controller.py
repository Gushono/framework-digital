import connexion

from server.controllers import util
from server.services import todos_service


def get_todos():
    """
    GET -> /todos

    List of todos.

    :return: TodoListSchema in swagger
    """
    params: dict = util.get_params(connexion)
    return todos_service.get_todos(params)


def get_todos_by_id(id_todo: int):
    """
    GET -> /todos/{id}

    Object of TODOS by id.

    :return: TodoSchema in swagger
    """
    return todos_service.get_todos_by_id(id_todo)
