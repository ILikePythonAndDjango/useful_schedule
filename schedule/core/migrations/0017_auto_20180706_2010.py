# Generated by Django 2.0.5 on 2018-07-06 20:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20180706_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='goals',
        ),
        migrations.AlterField(
            model_name='goal',
            name='begin',
            field=models.DateField(default=datetime.datetime(2018, 7, 6, 20, 10, 0, 794153, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='begin',
            field=models.TimeField(default=datetime.datetime(2018, 7, 6, 20, 10, 0, 816494, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.TimeField(default=datetime.datetime(2018, 7, 6, 20, 10, 0, 816693, tzinfo=utc)),
        ),
    ]