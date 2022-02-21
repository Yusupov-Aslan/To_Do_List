# Generated by Django 4.0 on 2022-02-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_Do_list', '0011_alter_projectuser_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuser',
            name='role',
            field=models.CharField(choices=[('project_manager', 'Менеджер проекта'), ('team_lead', 'Капитан'), ('developer', 'Разработчик')], default='project_manager', max_length=255, verbose_name='Должность'),
        ),
    ]