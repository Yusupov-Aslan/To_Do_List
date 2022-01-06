from django.shortcuts import render, redirect, get_object_or_404
from To_Do_list.models import Task, STATUS_CHOICES


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
    # try:
    #     task = Task.objects.get(pk=pk)
    # except Task.DoesNotExist:
    #     raise Http404
    task = get_object_or_404(Task, pk=pk)
    context = {"task": task}
    return render(request, 'one_task.html', context)


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_update.html', {"task": task, "status": STATUS_CHOICES})
    else:
        task.status = request.POST.get('status')
        task.description = request.POST.get('description')
        task.detailed_description = request.POST.get('detailed_description')
        task.to_do_at = request.POST.get('to_do_at')
        task.save()
        return redirect("one_task_view", pk=task.pk)


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', {"task": task})
    else:
        task.delete()
        return redirect('view_tasks_view')
