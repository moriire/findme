# Generated by Django 4.2.5 on 2023-10-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_bio_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='bio',
            name='profession',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
