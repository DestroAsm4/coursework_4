from flask_restx import Namespace, Resource
from project.container import auth_service, user_service
from project.setup.api.models import auth, auth_result
from flask import request


api = Namespace('auth')

@api.route('/register/')
class AuthView(Resource):
    @api.expect(auth)
    @api.response(201, description='OK')
    def post(self):
        """
        Регистрация пользователя
        """
        user_service.create(request.json)
        return 'OK', 201

@api.route('/login/')
class AuthView(Resource):
    @api.expect(auth)
    @api.marshal_with(auth_result, code=200)
    def post(self):
        """
        Аутентификация пользователя
        """
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)


        if None in [email, password]:
            return 'Email and password are required fields', 400

        token = auth_service.generate_tokens(email, password)

        return token, 200

    def put(self):
        """
        Создание новой пары токенов
        """

        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)


        return tokens, 200