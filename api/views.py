from django.shortcuts import render

# Create your views here.
from .models import User , TodoModel

from .serializers import TodoSerializer , UserSerializer

from rest_framework import viewsets
from rest_framework.response import Response

class TodoViewset(viewsets.ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    def  get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)
    
    
