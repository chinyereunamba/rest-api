from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('notes/', view_notes),
    path('notes/create/', create_note),
    path('notes/note/<int:pk>/', read_note),
    path('notes/note/<int:pk>/update', update_note),
    path('notes/note/<int:pk>/delete', delete_note),
]