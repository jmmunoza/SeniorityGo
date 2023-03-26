# Generated by Django 4.1.7 on 2023-03-26 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_profile_seniorities'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='seniorities',
            field=models.ManyToManyField(through='api.ProfileSeniority', to='api.seniority'),
        ),
    ]