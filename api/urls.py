from django.urls import path

from .views import TodoViewset

urlpatterns = [
    path('', TodoViewset.as_view(
        {
            'get': 'list',
            'post': 'create'
            
        }
    )),

]