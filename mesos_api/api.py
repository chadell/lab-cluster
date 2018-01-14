# pylint: disable=relative-import
from flask import Flask
from flask_restful import Api
from flask_login import LoginManager

from controllers.endpoints import EndpointsList
from controllers.services import (
    Services,
    ServiceID,
)
from controllers.instances import (
    InstanceID,
)
from controllers.auth import Auth
from controllers.models.user import User


def create_app():
    app = Flask(__name__)
    api = Api(app)
    # flask-login
    app.config.update(SECRET_KEY='secret_xxx')
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    # pylint: disable=unused-variable
    def load_user(user_id):
        return User(user_id)

    ##
    # API resource routing defined here
    ##
    api.add_resource(EndpointsList, '/')
    api.add_resource(Services, '/services', '/services/')
    api.add_resource(ServiceID, '/services/<service_name>')
    api.add_resource(InstanceID, '/services/<service_name>/<instance_name>')
    api.add_resource(Auth, '/auth/<token>')
    return app


def main():
    app = create_app()
    # listening in default port 5000
    app.run(threaded=True, debug=True, host='0.0.0.0')


if __name__ == '__main__':
    main()
