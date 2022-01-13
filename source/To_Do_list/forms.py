from django import forms
from django.forms import widgets

from To_Do_list.models import Type, Status


class TaskForm(forms.Form):
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    detailed_description = forms.CharField(max_length=2000, required=False, label='Подробное описание',
                                           widget=widgets.Textarea(attrs={"rows": 1, "cols": 40}))
    description = forms.CharField(max_length=2000, required=True, label="Описание",
                                  widget=widgets.Textarea(attrs={"rows": 1, "cols": 40}))
    to_do_at = forms.DateField(required=True, label="Дата выполнения")


