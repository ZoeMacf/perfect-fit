# Generated by Django 3.2.25 on 2024-06-12 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_userprofile_image'),
        ('user_msgs', '0003_remove_usermessage_puzzle_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='reciever',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='reciever',
            field=models.ManyToManyField(related_name='reciever', to='users.UserProfile'),
        ),
    ]