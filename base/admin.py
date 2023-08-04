from django.contrib import admin

from .models import Food, Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['task', 'completed', 'timestamp', 'updated']

admin.site.register(Food)
admin.site.register(Todo, TodoAdmin)