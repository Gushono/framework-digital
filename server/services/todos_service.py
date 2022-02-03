from typing import List

from flask import jsonify, Response

from server.configurations.constant import LIMIT_OF_TODOS
from server.configurations.logger import trace_logger
from server.repository.requester import RequestToJsonPlaceHolder


@trace_logger
def get_todos(params: dict) -> Response:
    """
    This function make the request in JsonPlaceHolderApi in the url /todos
    and return a list of todos formated.
    """

    todos_list = RequestToJsonPlaceHolder().get_method(path="/todos", params=params)

    new_todos_list = check_limit_of_todos(todos_list.copy())

    todo_formated = [format_todo_response(todo) for todo in new_todos_list]

    return jsonify(todo_formated)


@trace_logger
def get_todos_by_id(id_todo: int) -> Response:
    """
    This function make the request in JsonPlaceHolderApi in the url /todos/{id}
    and return a todos entity.

    :params: id_todo -> Id of todos entity.
    """
    todos = RequestToJsonPlaceHolder().get_method(path=f"/todos/{id_todo}")

    todo_formated = format_todo_response(todos, full_response=True)

    return jsonify(todo_formated)


def check_limit_of_todos(todos_list: List[dict]) -> List[dict]:
    """
    This function checks if there is any limit in the TODOs listing.
    If it exists, it shows only the first LIMIT_OF_TODOS elements. Otherwise, it returns the original list.

    :param: todos_list -> Original list of todos
    """
    if LIMIT_OF_TODOS is not None and isinstance(LIMIT_OF_TODOS, int):
        return todos_list[0:LIMIT_OF_TODOS]

    return todos_list


def format_todo_response(todos: dict, full_response=False) -> dict:
    """
    This function format the todos response.

    :params: todos -> Dict with info of a todos response
    :params: full_return -> Defines if the response needed is the entire payload or just resumed.
    """

    if not full_response:
        return {
            "id": todos.get("id"),
            "title": todos.get("title")
        }

    return todos
