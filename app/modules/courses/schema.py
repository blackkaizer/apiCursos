from flask_restx import fields

def course_model(api):
    return api.model("Course", {
        "id": fields.String(attribute="id"),
        "name": fields.String(required=True),
        "category": fields.String(required=True),
        "active": fields.Boolean,
        "created_at": fields.DateTime,
        "updated_at": fields.DateTime,
    })


def course_input_model(api):
    return api.model("CourseInput", {
        "name": fields.String(required=True),
        "category": fields.String(required=True),
        "active": fields.Boolean
    })
