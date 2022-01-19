from django import forms
from django.forms import CheckboxSelectMultiple, Textarea
from To_Do_list.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['type', 'status', 'summary', 'description']
        widgets = {'type': CheckboxSelectMultiple(), 'description': Textarea(attrs={"rows": 1, "cols": 24})}

