from django.urls import path
from .views import *

urlpatterns = [
    path('', get_food),
    path('post/', post_food)
]