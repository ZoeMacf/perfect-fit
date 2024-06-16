# Generated by Django 3.2.25 on 2024-06-16 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('msg_subject', models.CharField(blank=True, max_length=30, null=True)),
                ('msg_content', models.CharField(blank=True, max_length=240, null=True)),
                ('sent_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
