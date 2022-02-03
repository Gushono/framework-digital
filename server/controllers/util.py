def get_params(connexion):
    """
    Receive the query parameters from connexion.
    """
    params = {}

    for key in connexion.request.args:
        params[key] = connexion.request.args[key]

    return params
