# Generated by Django 5.1.2 on 2024-10-28 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_alter_users_email_alter_users_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Email',
            field=models.CharField(default='', max_length=15),
        ),
    ]
