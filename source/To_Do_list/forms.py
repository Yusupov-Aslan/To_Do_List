from django import forms
from django.forms import CheckboxSelectMultiple, Textarea
from To_Do_list.models import Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['type', 'status', 'summary', 'description']
        widgets = {'type': CheckboxSelectMultiple(), 'description': Textarea(attrs={"rows": 1, "cols": 24})}


class SearchForm(forms.Form):
    search = forms.CharField(max_length=40, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("date_begin", "date_end", "title", "description")