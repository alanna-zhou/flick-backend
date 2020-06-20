# Generated by Django 3.0.6 on 2020-06-19 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tag", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Show",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("ext_api_id", models.IntegerField(blank=True, null=True)),
                (
                    "ext_api_source",
                    models.CharField(
                        choices=[("tmdb", "TMDB"), ("animelist", "Animelist")], default=None, max_length=20
                    ),
                ),
                ("poster_pic", models.URLField(blank=True, null=True)),
                ("director", models.CharField(max_length=100)),
                ("is_tv", models.BooleanField()),
                ("date_released", models.DateField()),
                ("status", models.CharField(blank=True, max_length=100, null=True)),
                ("language", models.CharField(blank=True, max_length=100, null=True)),
                ("duration", models.DurationField(blank=True, null=True)),
                ("plot", models.TextField()),
                ("seasons", models.IntegerField(blank=True, null=True)),
                ("audience_level", models.CharField(blank=True, max_length=100, null=True)),
                ("imdb_rating", models.CharField(blank=True, max_length=10, null=True)),
                ("tomato_rating", models.CharField(blank=True, max_length=10, null=True)),
                ("platforms", models.CharField(blank=True, max_length=100, null=True)),
                ("keywords", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("tags", models.ManyToManyField(blank=True, to="tag.Tag")),
            ],
        ),
    ]
