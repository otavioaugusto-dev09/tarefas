from django.urls import path
from .views import task_list_create, task_handle

urlpatterns = [
    path('', task_list_create, name='task_list'),
    path('tasks/', task_list_create, name='task_list_create'),
    path('tasks/<int:task_id>/', task_handle, name='task_handle'),
]
