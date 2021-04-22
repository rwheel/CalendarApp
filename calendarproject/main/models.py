from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('main:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'



class ToDoList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
