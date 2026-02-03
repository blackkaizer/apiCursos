from flask import Flask
from flask_restx import Api
from .config import Config
from .extensions.db import init_db
from .extensions.jwt import init_jwt
from .modules.courses.controller import api as course_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)
    init_jwt(app)

    api = Api(
        app,
        title="Courses API",
        version="1.0",
        description="API de Cursos"
    )

    api.add_namespace(course_ns, path="/courses")

    return app
