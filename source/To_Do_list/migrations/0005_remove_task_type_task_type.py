# Generated by Django 4.0 on 2022-01-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_Do_list', '0004_alter_task_description_alter_task_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(related_name='tasks', to='To_Do_list.Type', verbose_name='Тип'),
        ),
    ]