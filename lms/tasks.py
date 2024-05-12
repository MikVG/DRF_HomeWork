from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from lms.models import Course, CourseSubscription
from users.models import User


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


@shared_task()
def check_last_login():
    one_month_ago = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago)
    for user in inactive_users:
        user.is_active = False
        user.save()
