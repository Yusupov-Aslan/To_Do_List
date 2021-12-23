from django.shortcuts import render

# Create your views here.
from To_Do_list.models import Task, STATUS_CHOICES


def index_view(request):
    return render(request, 'index.html')


def add_task_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {"status": STATUS_CHOICES})
    else:
        status = request.POST.get('status')
        description = request.POST.get('description')
        to_do_at = request.POST.get('to_do_at')
        new_task = Task.objects.create(status=status, description=description, to_do_at=to_do_at)

        return render(request, 'tasks_add.html', {"tasks": new_task})


def view_tasks_view(request):
    task = Task.objects.order_by("created_at")
    return render(request, 'tasks_view.html', {'tasks': task})

