# Generated by Django 3.2.25 on 2024-06-09 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_country',
            new_name='default_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_county',
            new_name='default_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_image',
            new_name='default_image',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_phone_number',
            new_name='default_phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_postcode',
            new_name='default_postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_street_address1',
            new_name='default_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_street_address2',
            new_name='default_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_town_or_city',
            new_name='default_town_or_city',
        ),
    ]
