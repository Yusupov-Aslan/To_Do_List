# Generated by Django 4.0 on 2022-01-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_Do_list', '0002_alter_task_description_alter_task_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='detailed_description',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='подробное описание'),
        ),
    ]
