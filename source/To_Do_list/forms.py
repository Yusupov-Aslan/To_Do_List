from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import CheckboxSelectMultiple, Textarea
from To_Do_list.models import Task, Project, ProjectUser


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['type', 'status', 'summary', 'description', 'project']
        widgets = {'type': CheckboxSelectMultiple(), 'description': Textarea(attrs={"rows": 1, "cols": 24})}


class SearchForm(forms.Form):
    search = forms.CharField(max_length=40, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("date_begin", "date_end", "title", "description")


class TaskFormProject(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['type', 'status', 'summary', 'description']
        widgets = {'type': CheckboxSelectMultiple(), 'description': Textarea(attrs={"rows": 1, "cols": 24})}


class ProjectDeleteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title",)

    def clean_title(self):
        if self.instance.title != self.cleaned_data.get("title"):
            raise ValidationError("Название статьи не соответствует")
        return self.cleaned_data.get("title")


class ParticipantAddForm(forms.ModelForm):
    class Meta:
        model = ProjectUser
        fields = ("user", "role")

    def __init__(self, *args, **kwargs):
        project_id = kwargs.pop('project_id', None)
        super().__init__(*args, **kwargs)
        participants = ProjectUser.objects.filter(project_id=project_id).values_list('user_id', flat=True)
        if project_id:
            self.fields['user'].queryset = User.objects.exclude(id__in=participants)
