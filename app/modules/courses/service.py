from datetime import datetime
from .model import Course

class CourseService:

    @staticmethod
    def create(data):
        course = Course(**data)
        course.save()
        return course

    @staticmethod
    def find_all():
        return Course.objects()

    @staticmethod
    def find_by_id(course_id):
        return Course.objects(id=course_id).first()

    @staticmethod
    def update(course_id, data):
        course = CourseService.find_by_id(course_id)
        if not course:
            return None

        for key, value in data.items():
            setattr(course, key, value)

        course.updated_at = datetime.utcnow()
        course.save()
        return course

    @staticmethod
    def delete(course_id):
        course = CourseService.find_by_id(course_id)
        if not course:
            return False

        course.delete()
        return True
