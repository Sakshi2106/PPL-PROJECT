# Generated by Django 3.0.6 on 2020-05-16 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecrime', '0004_newcase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecrime.SignUp'),
        ),
    ]
