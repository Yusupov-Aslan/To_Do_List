from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from To_Do_list.forms import ProjectForm
from To_Do_list.models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/view.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')


class ProjectCreateView(CreateView):
    template_name = 'projects/create.html'
    model = Project
    form_class = ProjectForm

    def get_redirect_url(self):
        return reverse('projects_view', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    template_name = 'projects/project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        comments = project.comments.order_by('-created_at')
        context['task'] = comments
        return context
