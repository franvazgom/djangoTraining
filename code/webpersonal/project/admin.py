from django.contrib import admin
from .models import Project

class ProjectAdmmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmmin)