# Generated by Django 3.2.25 on 2024-06-04 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaqContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=254, null=True)),
                ('answer', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]