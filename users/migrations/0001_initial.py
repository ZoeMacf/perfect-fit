# Generated by Django 3.2.25 on 2024-05-14 22:02

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(blank=True, max_length=20, null=True)),
                ('user_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('user_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('user_street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('user_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('user_town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('user_county', models.CharField(blank=True, max_length=80, null=True)),
                ('user_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('user_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]