# Generated by Django 3.0.6 on 2021-01-20 19:43

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("ext_api_genre_id", models.IntegerField(blank=True, null=True)),
                (
                    "ext_api_source",
                    models.CharField(
                        blank=True, choices=[("tmdb", "TMDB"), ("animelist", "Animelist")], max_length=20, null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
