# Generated by Django 5.1.2 on 2024-10-28 02:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_rename_birthday_users_birthday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Gender',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
