from django.contrib import admin
from .models import CV, Skill, Project

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname")
    filter_horizontal = ("skills", "projects")

admin.site.register(Skill)
admin.site.register(Project)