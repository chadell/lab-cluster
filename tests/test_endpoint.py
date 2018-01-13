import json
from mesos_api.controllers.endpoints import ENDPOINTS


def test_endpoint(app):
    app_client = app.test_client()
    response = app_client.get('/')
    assert json.loads(response.get_data()) == ENDPOINTS
