# Generated by Django 3.2.25 on 2024-06-16 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_msgs', '0002_alter_usermessage_receiver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='receiver',
            new_name='message_receiver',
        ),
    ]
