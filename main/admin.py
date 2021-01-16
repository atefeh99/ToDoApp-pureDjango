from django.contrib import admin

# Register your models here.

from .models import Todolist,Item

admin.site.register(Todolist)
admin.site.register(Item)
