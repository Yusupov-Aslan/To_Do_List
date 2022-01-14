from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from To_Do_list.forms import TaskForm
from To_Do_list.models import Task


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class AddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_create.html', {"form": form})

    def post(self, request, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            type = form.cleaned_data.get('type')
            status = form.cleaned_data.get('status')
            summary = form.cleaned_data.get('summary')
            description = form.cleaned_data.get('description')
            new_task = Task.objects.create(type=type, status=status,
                                           summary=summary, description=description)
            return redirect("one_task_view", pk=new_task.pk)
        else:
            return render(request, 'task_create.html', {"form": form})


class TasksView(View):
    def get(self, request):
        task = Task.objects.order_by("-created_at")
        context = {'tasks': task}
        return render(request, 'tasks_view.html', context)


class One_Task_View(TemplateView):
    template_name = 'one_task.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


class UpdateView(View):

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
            'type': task.type,
            'status': task.status,
            'summary': task.summary,
            'description': task.description

        })
        return render(request, 'task_update.html', {"task": task, "form": form})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
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
        return render(request, 'task_delete.html', {"task": task})

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        task.delete()
        return redirect('view_tasks_view')
