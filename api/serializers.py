from rest_framework import serializers
from .models import User , TodoModel

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    model = TodoModel
    fields = '__all__'
    extra_kwargs = {
        'user': {'required': False},
    }