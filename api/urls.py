from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewset,Registerview

router = DefaultRouter()
router.register(r'todos', TodoViewset, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', Registerview.as_view(), name='register'),
    
]

