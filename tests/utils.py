
HEADERS = {'Content-Type': 'application/json'}


def login_test(app_client):
    token = '12345678'
    return app_client.post('/auth/{}'.format(token), headers=HEADERS)
