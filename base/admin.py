from django.contrib import admin

from .models import Food, Todo

# Register your models here.

admin.site.register(Food)
admin.site.register(Todo)