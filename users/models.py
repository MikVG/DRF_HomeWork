from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True, verbose_name='почта', help_text='введите почту')
    phone = models.CharField(max_length=35, verbose_name='телефон',help_text='введите номер телефона',
                             blank=True, null=True)
    city = models.CharField(max_length=50, verbose_name='город',help_text='укажите город',
                               blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', help_text='прикрепите аватар',
                               blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.email}'
