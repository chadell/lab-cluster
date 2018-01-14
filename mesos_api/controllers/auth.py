# pylint: disable=relative-import
from flask import abort
from flask_restful import Resource
from flask_login import login_user
from models.user import User


class Auth(Resource):
    '''
    Endpoint /auth/<token>
    '''
    # pylint: disable=inconsistent-return-statements
    @staticmethod
    def post(token):
        token = token.strip('"')
        # Here a proper token validation should be implemented
        if token == '12345678':
            user = User(1)
            login_user(user)
            return "No Response", 204
        abort(403)
