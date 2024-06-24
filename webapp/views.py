from django.shortcuts import render

from webapp.models import ToDoList


# Create your views here.

def index(request):
    todo_lists = ToDoList.objects.order_by("deadline")
    return render(request,'index.html', context={"todo_lists": todo_lists})
