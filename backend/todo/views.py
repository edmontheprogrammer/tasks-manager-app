from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets):
    serializer_class = TodoSerializer
    quertset = Todo.objects.all()
