from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from lms.models import Course, CourseSubscription


@shared_task
def send_update_course(course_id):
    course = Course.objects.get(pk=course_id)
    course_subscribe = CourseSubscription.objects.filter(course=course_id)

    for subscribe in course_subscribe:
        send_mail(
            f'Обновление курса {course.title}',
            f'Обновление курса {course.title}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscribe.owner.email]
        )
