import json

def python_gcp_function(request):
    """Responds to any HTTP request.

    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:

        jsonmessage = {
            "message": "message via la cloud function: " + request_json['message']
        }

        # convert into JSON:
        return json.dumps(jsonmessage)
    else:
        return f'Hello World!'
