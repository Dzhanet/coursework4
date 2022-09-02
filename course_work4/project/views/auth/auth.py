from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service, user_service

api = Namespace('auth')


@api.route("/register/")
class AuthView(Resource):
    def post(self):
        """Регистрация пользователя"""
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@api.route('/login/')
class AuthView(Resource):
    def post(self):
        """Идентификация пользователя"""
        req_json = request.json
        email = req_json.get('email')
        password = req_json.get('password')
        if None in [email, password]:
            return "Нужно email и пароль", 400
        tokens = auth_service.generate_tokens(email, password)
        if tokens != False:
            return tokens, 201
        else:
            return "Ошибка в запросе", 400
