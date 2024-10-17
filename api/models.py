from django.db import models

class User(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def  __str__(self):
        return self.username


class TodoModel(models.Model):

    title = models.CharField(max_length=50 , primary_key= True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed  = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.title
    
# Create your models here.
