from django import forms
from django.forms import widgets

from To_Do_list.models import Type, Status


class TaskForm(forms.Form):
    type = forms.ModelChoiceField(queryset=Type.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    summary = forms.CharField(max_length=20, required=True, label="Краткое описание")
    description = forms.CharField(max_length=2000, required=True, label="Полное описание",
                                  widget=widgets.Textarea(attrs={"rows": 1, "cols": 40}))


