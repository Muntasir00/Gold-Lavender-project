from django.contrib import admin
from .models import Mobile

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'model_name', 'color', 'jan_code']
    list_filter = ['jan_code']

