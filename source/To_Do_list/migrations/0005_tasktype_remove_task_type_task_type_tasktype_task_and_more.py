# Generated by Django 4.0 on 2022-01-15 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('To_Do_list', '0004_alter_task_description_alter_task_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='tasks', through='To_Do_list.TaskType', to='To_Do_list.Type'),
        ),
        migrations.AddField(
            model_name='tasktype',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Task', to='To_Do_list.task', verbose_name='Задача'),
        ),
        migrations.AddField(
            model_name='tasktype',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Type', to='To_Do_list.type', verbose_name='Тип'),
        ),
    ]
