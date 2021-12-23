from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=20, default='new', choices=STATUS_CHOICES, verbose_name='Статус')
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    to_do_at = models.CharField(max_length=20, null=True, blank=False, verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.pk}. {self.description}: {self.status}"

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
