# Generated by Django 5.0.4 on 2024-04-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_payment_paid_course_alter_payment_paid_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(verbose_name='дата оплаты'),
        ),
    ]
