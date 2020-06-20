# Generated by Django 3.0.6 on 2020-06-19 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("asset", "0001_initial"),
        ("show", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lst",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("lst_name", models.CharField(max_length=100)),
                ("is_favorite", models.BooleanField(default=False)),
                ("is_private", models.BooleanField(default=False)),
                ("is_watched", models.BooleanField(default=False)),
                (
                    "collaborators",
                    models.ManyToManyField(blank=True, related_name="collaborators", to=settings.AUTH_USER_MODEL),
                ),
                (
                    "lst_pic",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="asset.AssetBundle"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="owner", to=settings.AUTH_USER_MODEL
                    ),
                ),
                ("shows", models.ManyToManyField(blank=True, to="show.Show")),
            ],
        ),
    ]
