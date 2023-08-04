from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, status

from .serializer import *

# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello Django REST Framework</h1>')


class NotesView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


'''CRUD with separate class based views (CBV)'''
class CreateNote(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class ViewNote(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class EditNote(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class DeleteNote(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


view_notes = NotesView.as_view()

create_note = CreateNote.as_view()      # C
read_note = ViewNote.as_view()          # R
update_note = EditNote.as_view()        # U
delete_note = DeleteNote.as_view()      # D
