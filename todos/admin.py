from django.contrib import admin
from .models import Task


class TaskDisplay(admin.ModelAdmin):
    list_display = ['task', 'is_completed', 'created_at']
    search_fields = ['task']


# Register your models here.
admin.site.register(Task, TaskDisplay)
