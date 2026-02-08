from datetime import datetime
from .model import User
from flask_jwt_extended import create_access_token

class AuthService:

    @staticmethod
    def create_user(data):
        user = User(**data)
        user.set_password(data['password'])
        user.save()
        return user

    @staticmethod
    def find_user(username):
        user = User.objects.get(username=username)
        return user

    @staticmethod
    def update_user(data):
        try:
            user = User.objects.get(username=data['username'])
            if not user:
                return None

            first_name = data['first_name']
            last_name = data['last_name']

            user.first_name = first_name
            user.last_name = last_name
            user.updated_at = datetime.now()
            user.save()
            return user
        except Exception as e:
            return {"message": str(e)}, 401

    @staticmethod
    def delete_user(username):
        user = User.objects.get(username=username)
        if not user:
            return None

        user.delete()
        return True

    @staticmethod
    def inative_user(username):
        user = User.objects.get(username=username)
        if not user:
            return None
        user.is_active = False
        user.updated_at = datetime.now()
        user.save()
        return

    @staticmethod
    def login_user(data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"message": "Username and password are required."}, 400

        user = AuthService.find_user(username)

        if not user or not user.check_password(password):
            return {"message": "Invalid username or password."}, 401

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "username": user.username,
                "email": user.email,
                "is_admin": user.is_admin,
            }
        )

        return {"access_token": access_token}, 200
