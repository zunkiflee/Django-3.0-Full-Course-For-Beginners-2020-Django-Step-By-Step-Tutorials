# Generated by Django 3.0.2 on 2020-01-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoprtNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]