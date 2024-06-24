from django.contrib import admin

from webapp.models import ToDoList


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'deadline']
    list_display_links = ['id', 'description', 'status']
    list_filter = ['deadline']
    search_fields = ['id', 'deadline']
    fields = ['description', 'status', 'deadline']
    # readonly_fields = ['created_at', 'updated_at']


# Register your models here.
admin.site.register(ToDoList, ToDoListAdmin)
