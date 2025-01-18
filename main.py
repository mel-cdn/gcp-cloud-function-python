def handler(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    print(f"Request METHOD: {request.method}")
    print(f"Request URL: {request.url}")

    req_args = request.args
    print(f"Request ARGS: {req_args}")
    req_body = request.get_json(silent=True)
    print(f"Request BODY: {req_body}")


    if req_body and 'name' in req_body:
        name = req_body['name']
    elif req_args and 'name' in req_args:
        name = req_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(name)
