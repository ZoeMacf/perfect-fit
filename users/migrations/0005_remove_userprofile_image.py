# Generated by Django 3.2.25 on 2024-06-12 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userprofile_display_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]