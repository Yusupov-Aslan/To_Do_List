from django.contrib import admin

from To_Do_list.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'description', 'created_at']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['status', 'description', 'created_at', 'to_do_at']
    readonly_fields = ['created_at']


admin.site.register(Task, TaskAdmin)
