from django.contrib import admin

from To_Do_list.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'type', 'description', 'created_at']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['type', 'status', 'summary', 'description']
    readonly_fields = ['created_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)
