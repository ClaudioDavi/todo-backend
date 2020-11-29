from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import TaskSerializer, TaskListSerializer
from .models import Task, TaskList


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "All Tasks": "GET: /tasks/",
        "Create Task": "POST: /tasks/",
        "Update Task": "PUT: /tasks/<str:key>/",
        "View Task": "GET: /tasks/<str:key>/",
        "Delete Task": "DELETE: /tasks/<str:key>/",
    }
    return Response(api_urls)


@api_view(["GET", "POST"])
def task(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except Exception as e:
            print(e)
            raise e
        
        
        return Response(serializer.data)
    


@api_view(["GET", "PUT", "DELETE"])
def single_task(request, key):
    tasks = Task.objects.get(id=key)
    if request.method == "GET":
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = TaskSerializer(instance=tasks, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    if request.method == "DELETE":
        tasks.delete()
        return Response("Task with Id {} deleted successfully".format(key))


@api_view(["GET", "POST"])
def task_list(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def single_task_list(request, key):
    task_lists = TaskList.objects.get(id=key)
    if request.method == "GET":
        serializer = TaskListSerializer(task_lists, many=False)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = TaskListSerializer(instance=task_lists, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    if request.method == "DELETE":
        task_lists.delete()
        return Response("Task List with Id {} deleted successfully".format(key))