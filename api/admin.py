from django.contrib import admin

from .models import Note, Tag

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    readonly_fields = ['created', 'updated']

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'date_created']

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)