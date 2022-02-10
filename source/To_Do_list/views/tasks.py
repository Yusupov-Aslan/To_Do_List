from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from To_Do_list.forms import TaskForm, SearchForm
from To_Do_list.models import Task


class IndexView(View):
    def get(self, request):
        return render(request, 'tasks/index.html')


class AddView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create.html"

    def get_success_url(self):
        return reverse("To_Do_list:one_task_view", kwargs={"pk": self.object.pk})


class TasksView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/view.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None


class One_Task_View(DetailView):
    template_name = 'tasks/one_task.html'
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse("To_Do_list:one_task_view", kwargs={"pk": self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/delete.html'

    def get_success_url(self):
        task = get_object_or_404(Task, id=self.kwargs.get('pk'))
        project_id = task.project_id
        return reverse("To_Do_list:project_view", kwargs={'pk': project_id})

