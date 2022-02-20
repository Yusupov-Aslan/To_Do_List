from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from To_Do_list.models import Project, Task
from To_Do_list.forms import ProjectForm, TaskFormProject, ProjectDeleteForm, ParticipantAddForm


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/view.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('title')


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create.html'

    def get_success_url(self):
        return reverse("To_Do_list:project_view", kwargs={"pk": self.object.pk})


class ProjectDetailView(DetailView):
    template_name = 'projects/project.html'
    model = Project

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['participants'] = self.object.participants.all()
    #     return context


class ProjectTaskAdd(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskFormProject
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        print(project)
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('To_Do_list:project_view', pk=project.pk)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/update.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("To_Do_list:project_view", kwargs={"pk": self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('To_Do_list:projects_view')
    form_class = ProjectDeleteForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method == "POST":
            kwargs['instance'] = self.object
        return kwargs


class ProjectParticipantAdd(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/participant_add.html'
    form_class = ParticipantAddForm

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        form = self.get_form()
        if form.is_valid():
            pru = form.save(commit=False)
            pru.project = project
            pru.save()
            return redirect('To_Do_list:project_view', pk=project.pk)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        form = ParticipantAddForm()
        return render(request, self.template_name, {'form': form, 'project': self.get_object()})


class ProjectParticipantDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('To_Do_list:project_view')

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        user_id = request.POST.get('user_id')
        project.participants.remove(user_id)
        return redirect('To_Do_list:project_view', pk=project.pk)

