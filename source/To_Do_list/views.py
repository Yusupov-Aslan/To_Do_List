from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView, ListView

from To_Do_list.base import FormView as CustomFormView
from To_Do_list.forms import TaskForm
from To_Do_list.models import Task


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class AddView(CustomFormView):
    form_class = TaskForm
    template_name = "task_create.html"

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect("one_task_view", pk=self.object.pk)


class TasksView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks_view.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    # def get_objects(self):
    #     return Task.objects.order_by('-created_at')


class One_Task_View(TemplateView):
    template_name = 'one_task.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


class UpdateView(FormView):
    template_name = 'task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('one_task_view', kwargs={'pk': self.task.pk})

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))


class DeleteView(View):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        return render(request, 'task_delete.html', {"task": task})

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        task.delete()
        return redirect('view_tasks_view')
