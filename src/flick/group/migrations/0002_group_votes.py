# Generated by Django 3.1.5 on 2021-01-30 00:37

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vote", "0001_initial"),
        ("group", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="votes",
            field=models.ManyToManyField(blank=True, to="vote.Vote"),
        ),
    ]
