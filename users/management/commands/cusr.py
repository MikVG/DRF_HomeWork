from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='Student1@admin.com',
        )
        user.set_password('12345')
        user.save()

        user = User.objects.create(
            email='Student2@admin.com',
        )
        user.set_password('12345')
        user.save()