# Generated by Django 4.2.7 on 2025-03-06 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoscrape',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='videoscrape',
            name='subscribers',
        ),
    ]
