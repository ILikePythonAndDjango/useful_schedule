# Generated by Django 2.0.5 on 2018-08-03 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180717_0734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='costcontrol',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='goal',
            name='begin',
            field=models.DateField(default=datetime.datetime(2018, 8, 3, 16, 42, 55, 663214, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='begin',
            field=models.TimeField(default=datetime.datetime(2018, 8, 3, 16, 42, 55, 686251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.TimeField(default=datetime.datetime(2018, 8, 3, 16, 42, 55, 686463, tzinfo=utc)),
        ),
    ]
