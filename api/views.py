from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import TaskSerializer, TaskListSerializer
from .models import Task, TaskList


@api_view(["GET", "POST"])
def task(request):
    """
    GET: Return All Tasks
    POST: Creates new Task

    """
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
    """
    GET: Retunrs a specifc task
    PUT: Edit a task
    DELETE: Deletes a task
    """
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
    """
    GET: return all tasks lists POST: Create new Task list
    """
    if request.method == "GET":
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def single_task_list(request, key):
    """
    Read, Edit or Delete a specific Task List
    """
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


@api_view(["GET"])
def get_tasks_by_task_list(request, key):
    """
    Get all tasks inside a task list.
    """
    if request.method == "GET":
        tasks = Task.objects.filter(task_list__id=key)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)