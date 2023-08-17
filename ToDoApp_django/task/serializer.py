from rest_framework import serializers
from task.models import Todo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        exclude=["updated_at"]