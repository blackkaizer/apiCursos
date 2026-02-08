from datetime import datetime, timezone
from mongoengine import Document, StringField, BooleanField, DateTimeField
from werkzeug.security import generate_password_hash, check_password_hash

class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    is_admin = BooleanField(default=False)
    is_active = BooleanField(default=True)
    password = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    meta = {
        "collection": "users"
    }