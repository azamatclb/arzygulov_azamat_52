from django.urls import path

from webapp.views import index, create_task, task_detail

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_task, name='create_task'),
    path('task/', views.task_detail, name='task_detail'),]