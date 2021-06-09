# Generated by Django 3.2.3 on 2021-06-02 16:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0002_typeservice_usertypeservice'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usertypeservice',
            unique_together={('user', 'type_service')},
        ),
    ]