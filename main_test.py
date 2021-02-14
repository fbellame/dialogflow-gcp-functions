import flask
import pytest

import main


# Create a fake "app" for generating test request contexts.
@pytest.fixture(scope="module")
def app():
    return flask.Flask(__name__)

def test_python_gcp_function(app):
    with app.test_request_context():
        res = main.python_gcp_function(flask.request)
        assert 'Hello World!' in res