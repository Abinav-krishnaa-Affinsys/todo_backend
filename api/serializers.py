from rest_framework import serializers
from .models import User , TodoModel

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    model = TodoModel
    fields = '__all__'
    read_only_fields = [
        'id'
        'created_at'
        'completed'
    ]
    write_only_fields = [
        'title',
        'description'
        
    ]
    
    