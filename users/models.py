from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson


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


class Payment(models.Model):

    mode = [
        ('cash', 'наличные'),
        ('bank', 'банковский перевод')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', null=True,
                                    blank=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', null=True,
                                    blank=True)
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_mode = models.CharField(max_length=25, verbose_name='способ оплаты', choices=mode, default='cash')

    def __str__(self):
        return f'{self.user}, {self.amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
