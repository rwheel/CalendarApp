from django.contrib import admin

from .models import ToDoList, Item, Event

admin.site.register(ToDoList)
admin.site.register(Item)

admin.site.register(Event)
