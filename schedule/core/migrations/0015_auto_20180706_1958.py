# Generated by Django 2.0.5 on 2018-07-06 19:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180705_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('thing', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='goal',
            name='begin',
            field=models.DateField(default=datetime.datetime(2018, 7, 6, 19, 58, 19, 676413, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='begin',
            field=models.TimeField(default=datetime.datetime(2018, 7, 6, 19, 58, 19, 698648, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.TimeField(default=datetime.datetime(2018, 7, 6, 19, 58, 19, 698871, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='note',
            name='cost_control',
            field=models.ManyToManyField(blank=True, to='core.CostControl'),
        ),
    ]
