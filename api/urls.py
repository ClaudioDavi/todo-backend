from django.urls import path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="Todo API",
            description="API Documentation for TODO Project",
            version="0.1.0",
        ),
        name="todo-schema",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="swagger-ui.html", extra_context={"schema_url": "todo-schema"}
        ),
        name="swagger-ui",
    ),
    path("tasks/", views.task, name="tasks"),
    path("tasks/<str:key>/", views.single_task, name="single-task"),
    path("task-lists/", views.task_list, name="task-list"),
    path("task-lists/<str:key>/", views.single_task_list, name="single-task-list"),
]
