from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def home(request):
    return HttpResponse('<h1>This is a basic http response</h1>')

@api_view(['GET'])
def get_food(request):
    return Response()

def post_food(request):
    return Response()