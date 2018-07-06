# Generated by Django 2.0.5 on 2018-07-06 20:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20180706_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='begin',
            field=models.DateField(default=datetime.datetime(2018, 7, 6, 20, 6, 27, 800277, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='note',
            name='goals',
        ),
        migrations.AddField(
            model_name='note',
            name='goals',
            field=models.ManyToManyField(blank=True, to='core.Goal'),
        ),
        migrations.AlterField(
            model_name='task',
            name='begin',
            field=models.TimeField(default=datetime.datetime(2018, 7, 6, 20, 6, 27, 874338, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.TimeField(default=datetime.datetime(2018, 7, 6, 20, 6, 27, 874785, tzinfo=utc)),
        ),
    ]
