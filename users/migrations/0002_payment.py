# Generated by Django 5.0.4 on 2024-04-16 17:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(verbose_name='дата оплаты')),
                ('amount', models.PositiveIntegerField(verbose_name='сумма оплаты')),
                ('payment_mode', models.CharField(choices=[('cash', 'наличные'), ('bank', 'банковский перевод')], default='cash', max_length=25, verbose_name='способ оплаты')),
                ('paid_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='оплаченный курс')),
                ('paid_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]
