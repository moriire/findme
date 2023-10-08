# Generated by Django 4.2.5 on 2023-10-08 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100)),
                ('project_title', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('count', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('hired', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_circle', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
