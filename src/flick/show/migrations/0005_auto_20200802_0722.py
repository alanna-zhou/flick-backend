# Generated by Django 3.0.6 on 2020-08-02 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("show", "0004_auto_20200802_0708")]

    operations = [
        migrations.AlterUniqueTogether(
            name="show", unique_together={("title", "ext_api_id", "ext_api_source", "poster_pic", "date_released")}
        )
    ]
