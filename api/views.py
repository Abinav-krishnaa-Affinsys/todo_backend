from django.shortcuts import render

# Create your views here.
from .models import User , TodoModel

from .serializers import TodoSerializer , UserSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TodoViewset(viewsets.ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    def  get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)
    def  perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
