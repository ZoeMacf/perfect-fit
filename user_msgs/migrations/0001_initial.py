# Generated by Django 3.2.25 on 2024-06-14 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("msg_content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "receiver",
                    models.ManyToManyField(
                        related_name="receiver", to="users.UserProfile"
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to="users.userprofile",
                    ),
                ),
            ],
        ),
    ]
