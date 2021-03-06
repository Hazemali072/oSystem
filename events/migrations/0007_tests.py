# Generated by Django 3.1.1 on 2020-10-06 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0006_events_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.DurationField(blank=True, null=True)),
                ('country', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('emails', models.TextField()),
                ('complete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('notification', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'tests',
            },
        ),
    ]
