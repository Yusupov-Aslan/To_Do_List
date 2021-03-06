# Generated by Django 4.0 on 2022-01-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_Do_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='detailed_description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='to_do_at',
        ),
        migrations.AddField(
            model_name='task',
            name='summary',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='task',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время обновления'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Полное описание'),
        ),
    ]
