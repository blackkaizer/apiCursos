import os

class Config:
    MONGODB_SETTINGS = {
        "db": os.getenv("MONGO_DB"),
        "host": os.getenv("MONGO_HOST"),
        "port": 27017,
        "username": os.getenv("MONGO_USER"),
        "password": os.getenv("MONGO_PASS"),
        "authentication_source": "admin"
    }

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")