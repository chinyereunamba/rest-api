from rest_framework import serializers

from .models import Note, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'note', 'user', 'tags']
        read_only_fields = ['id', 'user']
