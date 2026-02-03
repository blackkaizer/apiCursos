from datetime import datetime, timezone
from mongoengine import Document, StringField, BooleanField, DateTimeField

class Course(Document):
    name = StringField(required=True)
    category = StringField(required=True)
    active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))

    meta = {
        "collection": "courses"
    }