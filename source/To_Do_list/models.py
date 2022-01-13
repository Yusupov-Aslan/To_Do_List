from django.db import models

# Create your models here.


class Task(models.Model):
    summary = models.CharField(max_length=20, null=True, blank=True, verbose_name="Краткое описание")
    description = models.TextField(max_length=2000, verbose_name="Описание")
    status = models.ForeignKey('To_Do_list.Status', on_delete=models.PROTECT, related_name='Status', verbose_name='Статус')
    type = models.ForeignKey('To_Do_list.Type', on_delete=models.PROTECT, related_name='Type', verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f"{self.pk}. {self.summary}: {self.status} - {self.type}"

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Type(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.type}'

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Status(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
