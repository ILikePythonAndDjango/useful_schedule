# Generated by Django 2.0.5 on 2018-07-01 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_goal_sub_goals'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.TypeGoal'),
        ),
    ]
