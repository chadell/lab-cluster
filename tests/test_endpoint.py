import json
from mesos_api.controllers.endpoints import ENDPOINTS
from .utils import login_test


def test_endpoints_no_auth(app):
    app_client = app.test_client()
    response = app_client.get('/')
    assert response.status_code == 401


def test_endpoints(app):
    app_client = app.test_client()

    login_test(app_client)

    response = app_client.get('/')
    assert json.loads(response.get_data()) == ENDPOINTS
