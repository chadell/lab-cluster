from flask_restful import reqparse
from marathon.exceptions import MarathonError
from marathon.models import MarathonApp
from .mesosapi import ApiMesos


class Services(ApiMesos):
    '''
    Endpoint /services
    '''
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('service', type=str, location='json')
        super(Services, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        docker_setup = {"docker": {"image": args['service']}, "type": "DOCKER", "volumes": []}

        try:
            return str(self.c.create_app(args['service'],
                                         MarathonApp(container=docker_setup, mem=32.0, cpus=0.2, instances=1))), 201
        except MarathonError as mhe:
            return "Marathon API error: {}".format(mhe), 503

    def get(self):
        try:
            return [str(x) for x in self.c.list_apps()]
        except MarathonError as mhe:
            return "Marathon API error: {}".format(mhe), 503


class ServiceID(ApiMesos):
    '''
    Endpoint /services/<service_name>
    '''
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('action', type=str, location='args')
        super(ServiceID, self).__init__()

    def get(self, service_name):
        try:
            return str(self.c.list_tasks(service_name))
        except MarathonError as mhe:
            return "Marathon API error: {}".format(mhe), 503

    def delete(self, service_name):
        try:
            return str(self.c.delete_app(service_name))
        except MarathonError as mhe:
            return "Marathon API error: {}".format(mhe), 503

    def put(self, service_name):
        args = self.reqparse.parse_args()
        try:
            if args['action']:
                if args['action'] == 'scaleup':
                    return self.c.scale_app(service_name,
                                            instances=self.c.get_app(service_name).instances + 1,
                                            force=True)
                elif args['action'] == 'scaledown':
                    return self.c.scale_app(service_name,
                                            instances=self.c.get_app(service_name).instances - 1,
                                            force=True)
                elif args['action'] == 'restart':
                    return self.c.restart_app(service_name)
                return "Parameter or argument not supported", 400
            else:
                return "Sorry, action parameter not provided", 400
        except MarathonError as mhe:
            return "Marathon API error: {}".format(mhe), 503
