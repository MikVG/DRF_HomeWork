from django.core.management import BaseCommand

from lms.models import Course, Lesson
from users.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):

        payments_list = [
            {'user': User.objects.get(pk=2),
             'payment_date': '2024-04-01',
             'paid_course': Course.objects.get(pk=1),
             'amount': 3000,
             'payment_mode': 'cash'},
            {'user': User.objects.get(pk=2),
             'payment_date': '2024-04-05',
             'paid_lesson': Lesson.objects.get(pk=5),
             'amount': 1000,
             'payment_mode': 'bank'},
            {'user': User.objects.get(pk=3),
             'payment_date': '2024-04-07',
             'paid_course': Course.objects.get(pk=2),
             'amount': 15000,
             'payment_mode': 'bank'},
            {'user': User.objects.get(pk=3),
             'payment_date': '2024-04-11',
             'paid_lesson': Lesson.objects.get(pk=1),
             'amount': 5000,
             'payment_mode': 'bank'}
        ]

        for payment in payments_list:
            Payment.objects.create(**payment)
