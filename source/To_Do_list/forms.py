from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    detailed_description = forms.CharField(max_length=2000, required=True, label='Подробное описание',
                                           widget=widgets.Textarea(attrs={"rows": 1, "cols": 40}))
    description = forms.CharField(max_length=2000, required=True, label="Описание",
                                  widget=widgets.Textarea(attrs={"rows": 1, "cols": 40}))
    to_do_at = forms.DateField(required=True, label="Дата выполнения")
