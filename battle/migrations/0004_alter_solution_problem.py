# Generated by Django 3.2.10 on 2022-01-19 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0003_alter_solution_judge_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='problem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='battle.problem', verbose_name='задача'),
        ),
    ]
