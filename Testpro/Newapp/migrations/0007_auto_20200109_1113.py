# Generated by Django 3.0.2 on 2020-01-09 04:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0006_auto_20200109_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdb',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 9, 4, 13, 24, 730820, tzinfo=utc)),
        ),
    ]
