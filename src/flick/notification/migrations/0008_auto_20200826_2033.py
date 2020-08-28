# Generated by Django 3.0.6 on 2020-08-26 20:33

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("user", "0003_remove_profile_ratings"), ("notification", "0007_notification_new_owner")]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="collaborators_added",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="added_to_lst_notification", to="user.Profile"
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="collaborators_removed",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="removed_from_lst_notification", to="user.Profile"
            ),
        ),
    ]
