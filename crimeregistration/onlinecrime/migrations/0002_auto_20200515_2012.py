# Generated by Django 3.0.6 on 2020-05-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecrime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='signup',
            name='signup_as',
            field=models.CharField(choices=[('1', 'User'), ('2', 'Employee')], default='User', max_length=1),
        ),
    ]
