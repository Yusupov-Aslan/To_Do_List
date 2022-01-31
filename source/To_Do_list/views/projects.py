from django.views.generic import ListView, CreateView, DetailView
from To_Do_list.models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/view.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('title')


class ProjectCreateView(CreateView):
    template_name = 'projects/create.html'
    model = Project
    fields = ['title', 'description', 'date_begin', 'date_end']


class ProjectDetailView(DetailView):
    template_name = 'projects/project.html'

    def get_queryset(self):
        return Project.objects.all()
