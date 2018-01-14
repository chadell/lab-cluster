from flask_restful import Resource
from flask_login import login_required


ENDPOINTS = {
    'Deploy a service': 'POST /services',
    'List of services': 'GET /services',
    'List service instances': 'GET /services/<service_name>',
    'Delete a service': 'DELETE /services/<service_name>',
    'Update a service': 'PUT /services/<service_name>?action=<scaleup, scaledown, restart>',
    'Get service/instance info': 'GET /services/<service_name>/<instance_id>',
    'Kill an instance': 'DELETE /services/<service_name>/<instance_id>',
}


class EndpointsList(Resource):

    decorators = [login_required]

    @staticmethod
    def get():
        return ENDPOINTS
