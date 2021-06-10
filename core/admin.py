from django.contrib import admin
from .models import Classes

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display=('titulo',)
