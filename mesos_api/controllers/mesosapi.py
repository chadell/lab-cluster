import os
from flask_restful import Resource
from marathon import MarathonClient

url = os.environ.get('MARATHON_URL')


class ApiMesos(Resource):
    def __init__(self):
        if url:
            self.c = MarathonClient(url)
        else:
            raise NotImplementedError("Without Marathon URL this API has no sense")
