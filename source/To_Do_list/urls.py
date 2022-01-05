from django.urls import path

from To_Do_list.views import index_view, add_task_view, view_tasks_view, one_task_view, task_update_view

urlpatterns = [
    path('', index_view, name='index'),
    path('new_task/', add_task_view, name='add_task_view'),
    path('view_tasks/', view_tasks_view, name='view_tasks_view'),
    path('task/<int:pk>/', one_task_view, name='one_task_view'),
    path('task/<int:pk>/update/', task_update_view, name='task_update_view')
]
