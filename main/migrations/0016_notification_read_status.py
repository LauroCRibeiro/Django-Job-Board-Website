# Generated by Django 3.0.7 on 2020-06-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_notification_receiver_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read_status',
            field=models.BooleanField(default=False),
        ),
    ]
