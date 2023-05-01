# Generated by Django 4.1.7 on 2023-05-01 19:52

import api.models.developer
import api.models.organization
import api.models.requirement
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
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('second_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('role', models.CharField(default='developer', max_length=50)),
                ('birthday', models.DateField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=api.models.developer.upload_to)),
                ('phone_number', models.CharField(max_length=20)),
                ('is_activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.organization.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='api.organization')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileSeniority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Seniority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seniorities', to='api.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.requirement.upload_to)),
                ('points', models.IntegerField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='api.organization')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileSeniorityRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_seniority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profileseniority')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.requirement')),
            ],
        ),
        migrations.AddField(
            model_name='profileseniority',
            name='requirements',
            field=models.ManyToManyField(through='api.ProfileSeniorityRequirement', to='api.requirement'),
        ),
        migrations.AddField(
            model_name='profileseniority',
            name='seniority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.seniority'),
        ),
        migrations.AddField(
            model_name='profile',
            name='seniorities',
            field=models.ManyToManyField(through='api.ProfileSeniority', to='api.seniority'),
        ),
        migrations.CreateModel(
            name='DeveloperRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField()),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.developer')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.requirement')),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField()),
                ('entrance_date', models.DateField()),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.developer')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
                ('seniority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.seniority')),
            ],
        ),
        migrations.AddField(
            model_name='developer',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.organization'),
        ),
        migrations.AddField(
            model_name='developer',
            name='profiles',
            field=models.ManyToManyField(through='api.DeveloperProfile', to='api.profile'),
        ),
        migrations.AddField(
            model_name='developer',
            name='requirements',
            field=models.ManyToManyField(through='api.DeveloperRequirement', to='api.requirement'),
        ),
        migrations.AddField(
            model_name='developer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='admin', max_length=50)),
                ('organization', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
