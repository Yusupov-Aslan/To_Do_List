# Generated by Django 4.0 on 2022-02-20 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('To_Do_list', '0007_project_task_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('project_manager', 'Менеджер проекта'), ('team_lead', 'Капитан'), ('developer', 'Разработчик')], default='project_manager', max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectusers', to='To_Do_list.project', verbose_name='Проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprojects', to='auth.user', verbose_name='Пользователь')),
            ],
        ),
    ]