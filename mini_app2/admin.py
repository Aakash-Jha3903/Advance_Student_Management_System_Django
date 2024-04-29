# admin.py
from django.contrib import admin
# from .models import Officials, OfficialsUser  # Updated import statement
from .models import  OfficialsUser  # Updated import statement
from django.contrib.auth.admin import UserAdmin

@admin.register(OfficialsUser)
class OfficialsUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'created_at', 'updated_at']
    search_fields = ['name']
    ordering = ['name']  # Change this to the field you want to use for ordering

