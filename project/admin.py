from django.contrib import admin
from .models import ProjectModel


@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'note', 'add_time')
    search_fields = ('name', 'note',)
