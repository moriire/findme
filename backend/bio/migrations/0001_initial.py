# Generated by Django 4.2.5 on 2023-10-08 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_bio', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('body', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
