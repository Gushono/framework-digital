from flask import jsonify, Response

from server.repository.requester import RequestToJsonPlaceHolder


def get_todos(params: dict) -> Response:
    """
    This function make the request in JsonPlaceHolderApi in the url /todos
    and return a list of todos formated.
    """

    todos_list = RequestToJsonPlaceHolder().get_method(path="/todos", params=params)

    todo_formated = [format_todo_response(todo, full_response=params.get("full_response")) for todo in todos_list]

    return jsonify(todo_formated)


def get_todos_by_id(id_todo: int) -> Response:
    """
    This function make the request in JsonPlaceHolderApi in the url /todos/{id}
    and return a todos entity.

    :params: id_todo -> Id of todos entity.
    """
    todos = RequestToJsonPlaceHolder().get_method(path=f"/todos/{id_todo}")

    todo_formated = format_todo_response(todos, full_response=True)

    return jsonify(todo_formated)


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
