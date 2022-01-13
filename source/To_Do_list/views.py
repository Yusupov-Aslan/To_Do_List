from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from To_Do_list.forms import TaskForm
from To_Do_list.models import Task


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


def add_task_view(request, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            detailed_description = form.cleaned_data.get('detailed_description')
            to_do_at = form.cleaned_data.get('to_do_at')
            new_task = Task.objects.create(description=description,
                                           detailed_description=detailed_description, to_do_at=to_do_at)
            return redirect("one_task_view", pk=new_task.pk)
        else:
            return render(request, 'task_create.html', {"form": form})


class TasksView(View):

    def get(self, request):
        task = Task.objects.order_by("created_at")
        context = {'tasks': task}
        return render(request, 'tasks_view.html', context)


class One_Task_View(TemplateView):
    template_name = 'one_task.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'type': task.type,
            'status': task.status,
            'summary': task.summary,
            'description': task.description

        })
        return render(request, 'task_update.html', {"task": task, "form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.type = form.cleaned_data.get('type')
            task.status = form.cleaned_data.get('status')
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')

            task.save()
            return redirect("one_task_view", pk=task.pk)
        else:
            return render(request, 'task_update.html', {"task": task, "form": form})


class DeleteView(View):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        if request.method == 'GET':
            return render(request, 'task_delete.html', {"task": task})
        else:
            task.delete()
            return redirect('view_tasks_view')
