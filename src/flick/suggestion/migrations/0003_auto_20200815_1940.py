# Generated by Django 3.0.7 on 2020-08-15 19:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_profile_ratings"),
        ("show", "0006_auto_20200802_0723"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("suggestion", "0002_auto_20200815_1935"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="privatesuggestion", unique_together={("message", "show", "from_user", "to_user")},
        ),
    ]
