# Generated by Django 3.0.2 on 2020-01-10 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0007_auto_20200109_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='newsdb',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 10, 14, 50, 16, 287951, tzinfo=utc)),
        ),
    ]
