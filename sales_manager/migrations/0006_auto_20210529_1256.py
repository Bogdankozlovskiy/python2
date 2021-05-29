# Generated by Django 3.2.3 on 2021-05-29 09:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales_manager', '0005_auto_20210526_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='likes',
        ),
        migrations.AddField(
            model_name='book',
            name='avg_rate',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.CreateModel(
            name='UserRateBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_manager.book')),
                ('user', models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'book')},
            },
        ),
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.ManyToManyField(blank=True, related_name='rated_book', through='sales_manager.UserRateBook', to=settings.AUTH_USER_MODEL),
        ),
    ]
