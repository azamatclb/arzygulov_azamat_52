from django.http import HttpResponseRedirect
from django.shortcuts import render

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
    try:
        task = ToDoList.objects.get(id=request.GET.get('id'))
    except ToDoList.DoesNotExist:
        return HttpResponseRedirect("/")
    return render(request, "view_detail.html", context={"task": task})
