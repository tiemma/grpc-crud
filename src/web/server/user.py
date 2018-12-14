from flask import json, request
from flask_restplus import Namespace, Resource, fields
from flask_restplus._http import HTTPStatus

from grpc_client.user.UserClient import create_user
from logger import Logger



USER_NS = Namespace("users", "User related operations")

USER = USER_NS.model('User', {
    'name': fields.String(required=True, description='The users name'),
    'email': fields.String(required=True, description='The users pet name'),
    'password': fields.String(description='User password sent on signup and login')
})


@USER_NS.route("/")
@USER_NS.response(HTTPStatus.NOT_FOUND, 'User not found')
class User(Resource):
    """
    User resource class for defining USER related API actions
    """
    logger = Logger.get_logger(__name__)

    @USER_NS.expect(USER, validate=True)
    def post(self):
        """
        :return:
        """
        try:
            response = create_user(request.json)
            self.logger.debug(response)

            if not response:
                return {'message': 'No response'}
        except IndexError as err:
            return {'message': err}

        del response['user']['password']
        return {"message": "User was successfully retrieved", "data": response}, HTTPStatus.OK
