from django.urls import path

from To_Do_list.views import index_view, add_task_view, view_tasks_view, one_task_view

urlpatterns = [
    path('', index_view),
    path('new_task/', add_task_view),
    path('view_tasks/', view_tasks_view),
    path('task/<int:pk>/', one_task_view)
]
