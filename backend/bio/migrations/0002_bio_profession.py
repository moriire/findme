# Generated by Django 4.2.5 on 2023-10-08 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='profession',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]