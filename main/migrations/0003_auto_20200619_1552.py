# Generated by Django 3.0.7 on 2020-06-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200618_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='password',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
