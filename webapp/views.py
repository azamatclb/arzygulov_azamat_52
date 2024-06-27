from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from webapp.models import ToDoList


# Create your views here.

def index(request):
    tasks = ToDoList.objects.order_by("deadline")
    return render(request, 'index.html', context={"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html")
    else:
        ToDoList.objects.create(
            description=request.POST.get("description"),
            status=request.POST.get("status"),
            deadline=request.POST.get("deadline")
        )
        return HttpResponseRedirect("/")


def task_detail(request):
    task_id = request.GET.get('id')
    task = get_object_or_404(ToDoList, id=task_id)
    return render(request, 'view_detail.html', {'task': task})
