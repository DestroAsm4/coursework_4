from project.setup.api.parsers import page_parser
from flask_restx import Namespace, Resource
from flask import request

from project.container import user_service
from project.setup.api.models import user

user_ns = Namespace('user')

@user_ns.route('/')
class UsersView(Resource):

    @user_ns.expect(page_parser)
    @user_ns.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        get all movies
        """
        return user_service.get_all(**page_parser.parse_args())



@user_ns.route('/<int:user_id>/')
class UserView(Resource):
    @user_ns.response(404, 'Not Found')
    @user_ns.marshal_with(user, code=200, description='OK')
    def get(self, user_id: int):
        """
        get movie by id
        """
        return user_service.get_one(user_id)

    @user_ns.response(404, 'Not Found')
    @user_ns.marshal_with(user, code=204, description='OK')
    def patch(self, user_id: int):
        """
        get movie by id
        """
        print(request.json)
        user_data = request.json
        user_service.update(user_data)

        return user_service.get_one(user_id)



    @user_ns.response(404, 'Not Found')
    @user_ns.response(204, description='OK')

    def put(self, user_id: int):
        """
        get movie by id
        """
        user = user_service.get_one(user_id)
        email = user.email
        data = request.json
        new_password = data['password']
        user = user_service.update_password(email, new_password)

        return 'OK', 200