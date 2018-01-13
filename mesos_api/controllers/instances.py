from flask_restful import reqparse
from marathon.exceptions import MarathonError
from .mesosapi import ApiMesos


class InstanceID(ApiMesos):
    '''
    Endpoint /services/<service_name>/<instance_name>
    '''
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('action', type=str, location='args')
        super(InstanceID, self).__init__()

    def get(self, service_name, instance_name):
        try:
            all_tasks = self.c.get_app(service_name).tasks
            for task in all_tasks:
                if task.id == instance_name:
                    return str(task)
            return "Sorry, your Instance ID is not part of this Service", 404
        except MarathonError as mhe:
            return "Marathon API error: {}".format(mhe), 503

    def delete(self, service_name, instance_name):
        args = self.reqparse.parse_args()
        try:
            if args['action']:
                if args['action'] == 'kill':
                    return self.c.kill_task(service_name, instance_name)
                return "Parameter or argument not supported", 400
            else:
                return "Sorry, action parameter not provided", 400
        except MarathonError as mhe:
            return "Marathon API error: {}".format(mhe), 503
