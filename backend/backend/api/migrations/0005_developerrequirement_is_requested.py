# Generated by Django 4.1.7 on 2023-06-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_validatefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='developerrequirement',
            name='is_requested',
            field=models.BooleanField(default=False),
        ),
    ]
