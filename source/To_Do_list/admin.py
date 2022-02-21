from django.contrib import admin
from django.contrib.auth.models import Permission

from To_Do_list.models import Task, Status, Type, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'description', 'created_at']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['type', 'status', 'summary', 'description', 'project']
    readonly_fields = ['created_at']
    filter_horizontal = ['type']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
admin.site.register(Permission)
