# Generated by Django 3.0.6 on 2020-05-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecrime', '0007_auto_20200518_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newcase',
            name='user',
        ),
        migrations.AddField(
            model_name='newcase',
            name='username',
            field=models.CharField(default='user', max_length=20),
        ),
    ]
