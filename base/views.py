from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Food
from .serializer import FoodSerializer

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