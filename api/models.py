from django.db import models
from django.utils import timezone


class TaskList(models.Model):
    title = models.CharField(max_length=100)


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    task_list = models.ForeignKey(TaskList, on_delete=models.SET_NULL, null=True)
    objects = models.Manager()
