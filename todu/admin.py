from django.contrib import admin
from .models import ToduModel,CategoriyModel


admin.site.register(CategoriyModel)


# Register your models here.
@admin.register(ToduModel)
class ToduModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_name', 'task_status']
    list_display_links = ['id', 'task_name']
    search_fields = ['task_name']
