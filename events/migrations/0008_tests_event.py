# Generated by Django 3.1.1 on 2020-10-06 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.events'),
            preserve_default=False,
        ),
    ]
