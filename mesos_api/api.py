# pylint: disable=relative-import
from flask import Flask
from flask_restful import Api
from controllers.endpoints import EndpointsList
from controllers.services import (
    Services,
    ServiceID,
)
from controllers.instances import (
    InstanceID,
)


def create_app():
    app = Flask(__name__)
    api = Api(app)

    ##
    # API resource routing defined here
    ##
    api.add_resource(EndpointsList, '/')
    api.add_resource(Services, '/services')
    api.add_resource(ServiceID, '/services/<service_name>')
    api.add_resource(InstanceID, '/services/<service_name>/<instance_name>')
    return app


def main():
    app = create_app()
    # listening in default port 5000
    app.run(threaded=True, debug=True, host='0.0.0.0')


if __name__ == '__main__':
    main()
