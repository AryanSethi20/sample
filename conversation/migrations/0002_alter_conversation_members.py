# Generated by Django 4.1.7 on 2023-04-03 06:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("conversation", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversation",
            name="members",
            field=models.ManyToManyField(
                related_name="users", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]