from .models import Food, Todo

from rest_framework import serializers

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'description']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task', 'timestamp', 'completed', 'updated', 'user']