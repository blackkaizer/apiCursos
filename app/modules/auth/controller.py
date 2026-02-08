from flask_restx import Namespace, Resource, reqparse
from flask_jwt_extended import jwt_required

from .service import AuthService
from .schema import user_model, input_user_model, user_login_model, user_update_model

api = Namespace("auth", description="Users operations")

@api.route("/login")
class Login(Resource):

    @api.expect(user_login_model(api))
    def post(self):
        """Fazer login"""
        return AuthService.login_user(api.payload)

@api.route("")
class Auth(Resource):

    @api.expect(input_user_model(api))
    @api.marshal_with(user_model(api))
    @jwt_required()
    @api.doc(security=[{'BearerAuth': []}])
    def post(self):
        """Cadastrar usuario"""
        return AuthService.create_user(api.payload)

    @jwt_required()
    @api.expect(user_update_model(api))
    @api.doc(security=[{'BearerAuth': []}])
    @api.marshal_with(user_model(api))
    def put(self):
        """Atualizar usuario"""
        return AuthService.update_user(api.payload)

@api.route("/<string:username>")
class User(Resource):
    @jwt_required()
    @api.doc(security=[{'BearerAuth': []}])
    @api.marshal_with(user_model(api))
    def get(self, username: str):
        """Buscar usuario"""
        user = AuthService.find_user(username)
        return user

    @jwt_required()
    @api.doc(security=[{'BearerAuth': []}])
    def delete(self, username: str):
        """Deletar usuario"""
        return AuthService.delete_user(username)

    @jwt_required()
    @api.doc(security=[{'BearerAuth': []}])
    def put(self, username: str):
        """Atualizar usuario"""
        return AuthService.inative_user(username)

