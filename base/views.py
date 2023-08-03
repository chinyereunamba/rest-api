from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Food, Todo
from .serializer import FoodSerializer, TodoSerializer

# Create your views here.


def home(request):
    return HttpResponse('<h1>This is a basic http response</h1>')


@api_view(['GET'])
def get_food(request):
    # Get queryset i.e. model
    food = Food.objects.all()

    # Then serializer the model data to json
    serializer = FoodSerializer(food, many=True)

    # return response as json i.e serialized model data
    return Response(serializer.data)


@api_view(['POST'])
def post_food(request):
    # gets data from the serializer using the request.data
    serializer = FoodSerializer(data=request.data)

    # checks if the serializer data is valid then saves
    if serializer.is_valid():
        serializer.save()

    # returns response as json
    return Response(serializer.data)


# AssertionError at /api/todo/ show up when @api_view is ommitted

@api_view(['GET'])
def get_todo(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def post_todo(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT', 'GET'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(todo, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
        if request.method == 'DELETE':
            todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
