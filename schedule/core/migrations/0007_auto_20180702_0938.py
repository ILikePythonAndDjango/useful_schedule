# Generated by Django 2.0.5 on 2018-07-02 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180702_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='begin',
            field=models.DateField(default=datetime.date(2018, 7, 2)),
        ),
    ]
