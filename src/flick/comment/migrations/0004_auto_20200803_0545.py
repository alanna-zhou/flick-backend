# Generated by Django 3.0.7 on 2020-08-03 05:45

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_profile_ratings"),
        ("comment", "0003_auto_20200802_2346"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comment", to="user.Profile"
            ),
        ),
    ]
