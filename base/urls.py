from django.urls import path
from .views import *

urlpatterns = [
    path('', get_food),
    path('post/', post_food),
    path('todo/', get_todo),
    path('todo/post/', post_todo),
    path('todo/post/<int:pk>/update/', update_todo),
    path('todo/post/<int:pk>/delete/', delete_todo),
]
