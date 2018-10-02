import logging

from flask import request
from flask_restplus import Resource
from api.directory.serializers import user
from api.restplus import api
from database.models import User

log = logging.getLogger(__name__)

ns = api.namespace('directory/users', description='User related operations')


@ns.route('/')
class UserCollection(Resource):

    # @api.marshal_list_with(user)
    def get(self):
        """
        Returns user list.
        """
        pass

    @api.response(200, 'User successfully created.')
    @api.expect(user)
    def post(self):
        """
        Creates a user.
        """
        data = request.json
        create_user(data)
        return None, 200


@ns.route('/<int:id>')
@api.response(404, 'User not found.')
class UserItem(Resource):

    # @api.marshal_with(user)
    def get(self, id):
        """
        Returns a user with.
        """
        return User.query.filter(User.id == id).one()
