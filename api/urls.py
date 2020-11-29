from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api_overview"),
    path("tasks/", views.task, name="tasks"),
    path("tasks/<str:key>/", views.single_task, name="single-task"),
    path("task-lists/", views.task_list, name="task-list"),
    path("task-lists/<str:key>/", views.single_task_list, name="single-task-list"),
]
