from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from To_Do_list.models import Project, Task
from To_Do_list.forms import ProjectForm, TaskFormProject


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/view.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('title')


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create.html'


class ProjectDetailView(DetailView):
    template_name = 'projects/project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = self.get_object().task
        context['task_id'] = tasks
        return context


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/view.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('title')


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create.html'

    def get_success_url(self):
        return reverse("project_view", kwargs={"pk": self.object.pk})


class ProjectDetailView(DetailView):
    template_name = 'projects/project.html'
    model = Project


class ProjectTaskAdd(CreateView):
    model = Task
    form_class = TaskFormProject
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        print(project)
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('project_view', pk=project.pk)
