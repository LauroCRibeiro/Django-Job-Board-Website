# Generated by Django 3.0.7 on 2020-06-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_applyjob_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='active_status',
            field=models.BooleanField(default=True),
        ),
    ]
