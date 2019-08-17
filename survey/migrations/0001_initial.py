# Generated by Django 2.2.4 on 2019-08-16 22:45

import datetime
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
            name='Organization',
            fields=[
                ('org_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('org_comment', models.CharField(blank=True, max_length=511, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Organization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_title', models.CharField(max_length=255)),
                ('survey_description', models.CharField(max_length=1023)),
                ('survey_approval_required', models.BooleanField()),
                ('survey_due_date', models.DateField()),
                ('survey_creation_date', models.DateField(default=datetime.date.today)),
                ('survey_archived', models.BooleanField(default=False)),
                ('survey_owner_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Organization')),
                ('survey_owner_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='survey.Profile')),
                ('survey_responsible_users', models.ManyToManyField(related_name='responsible_users', to='survey.Profile')),
            ],
        ),
    ]