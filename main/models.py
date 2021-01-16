from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todolist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True,related_name='todolist')
    name = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=300, blank=True, null=True)
    complete = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.text
