# Generated by Django 3.0.7 on 2020-08-06 00:43

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("comment", "0004_auto_20200803_0545"),
        ("user", "0003_remove_profile_ratings"),
        ("like", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="comment_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="likers", to="comment.Comment"
            ),
        ),
        migrations.AlterField(
            model_name="like",
            name="liker",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="likes", to="user.Profile"
            ),
        ),
    ]
