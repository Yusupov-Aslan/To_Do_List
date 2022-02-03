from django.db import models
from django.core.validators import BaseValidator

from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Значение "%(value)s" имеет длину %(show_value)d символа!Должно быть не менее %(limit_value)d символов!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


@deconstructible
class MaxLengthValidator(BaseValidator):
    message = 'Убедитесь, что это значение содержит не более %(limit_value)d символов (у него %(show_value)d). '
    code = 'max_length'

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return len(x)


class Task(models.Model):
    summary = models.CharField(max_length=20, verbose_name="Краткое описание", validators=(MinLengthValidator(5),))
    description = models.TextField(max_length=2000, null=True, blank=True,
                                   verbose_name="Полное описание", validators=(MaxLengthValidator(200),))
    status = models.ForeignKey('To_Do_list.Status', on_delete=models.PROTECT,
                               related_name='Status', verbose_name='Статус')
    type = models.ManyToManyField('To_Do_list.Type', related_name='tasks', verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    project = models.ForeignKey('To_Do_list.Project', on_delete=models.CASCADE, default=1, related_name='tasks',
                                verbose_name='Проект')

    def __str__(self):
        return f"{self.pk}. {self.summary}: {self.status} - {self.type}"

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.type}'

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Project(models.Model):
    date_begin = models.CharField(max_length=20, null=True, blank=False, verbose_name="Дата начала")
    date_end = models.CharField(max_length=20, null=True, blank=True, verbose_name="Дата окончания")
    title = models.CharField(max_length=20, verbose_name="Название", validators=(MinLengthValidator(5),))
    description = models.TextField(max_length=2000, null=True, blank=True,
                                   verbose_name="Описание", validators=(MaxLengthValidator(2000),))

    def __str__(self):
        return f"{self.pk}. {self.title}: {self.description}"

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

