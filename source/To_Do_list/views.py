from django.shortcuts import render, redirect
from To_Do_list.models import Task, STATUS_CHOICES
from django.http import Http404

def index_view(request):
    return render(request, 'index.html')


def add_task_view(request, **kwargs):
    if request.method == 'GET':
        return render(request, 'task_create.html', {"status": STATUS_CHOICES})
    else:
        status = request.POST.get('status')
        description = request.POST.get('description')
        detailed_description = request.POST.get('detailed_description')
        to_do_at = request.POST.get('to_do_at')
        new_task = Task.objects.create(status=status, description=description,
                                       detailed_description=detailed_description, to_do_at=to_do_at)
        # context = {"tasks": new_task}
        # url = reverse("one_task_view", kwargs={"pk": new_task.pk})
        # return HttpResponseRedirect(url)

        return redirect("one_task_view", pk=new_task.pk)

        # return render(request, 'tasks_add.html', context)


def view_tasks_view(request):
    task = Task.objects.order_by("created_at")
    context = {'tasks': task}
    return render(request, 'tasks_view.html', context)
    # return redirect("view_tasks_view", context)


def one_task_view(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        context = {"task": task}
    except Task.DoesNotExist:
        raise Http404

    return render(request, 'one_task.html', context)
