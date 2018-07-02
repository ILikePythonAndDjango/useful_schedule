# Generated by Django 2.0.5 on 2018-07-01 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180701_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='sub_goals',
        ),
        migrations.AddField(
            model_name='goal',
            name='sub_goals',
            field=models.ManyToManyField(blank=True, null=True, to='core.Goal'),
        ),
    ]