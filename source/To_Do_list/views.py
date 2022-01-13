from django.shortcuts import render, redirect, get_object_or_404
from To_Do_list.forms import TaskForm
from To_Do_list.models import Task


def index_view(request):
    return render(request, 'index.html')


def add_task_view(request, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', {"form": form})
    else:
        form = TaskForm(data=request.POST)
        status = request.POST.get('status')
        if form.is_valid():
            description = form.cleaned_data.get('description')
            detailed_description = form.cleaned_data.get('detailed_description')
            to_do_at = form.cleaned_data.get('to_do_at')
            new_task = Task.objects.create(status=status, description=description,
                                           detailed_description=detailed_description, to_do_at=to_do_at)
            return redirect("one_task_view", pk=new_task.pk)
        else:
            return render(request, 'task_create.html', {"form": form})


def view_tasks_view(request):
    task = Task.objects.order_by("created_at")
    context = {'tasks': task}
    return render(request, 'tasks_view.html', context)
    # return redirect("view_tasks_view", context)


def one_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {"task": task}
    return render(request, 'one_task.html', context)


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'detailed_description': task.detailed_description,
            'description': task.description,
            'to_do_at': task.to_do_at
        })
        return render(request, 'task_update.html', {"task": task, "form": form})
    else:
        form = TaskForm(data=request.POST)
        task.status = request.POST.get('status')
        if form.is_valid():
            task.description = form.cleaned_data.get('description')
            task.detailed_description = form.cleaned_data.get('detailed_description')
            task.to_do_at = form.cleaned_data.get('to_do_at')
            task.save()
            return redirect("one_task_view", pk=task.pk)
        else:
            return render(request, 'task_update.html', {"task": task, "form": form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', {"task": task})
    else:
        task.delete()
        return redirect('view_tasks_view')
