from django.urls import path

from To_Do_list.views import (add_task_view,
                              task_update_view,
                              IndexView,
                              One_Task_View,
                              TasksView,
                              DeleteView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new_task/', add_task_view, name='add_task_view'),
    path('view_tasks/', TasksView.as_view(), name='view_tasks_view'),
    path('task/<int:pk>/', One_Task_View.as_view(), name='one_task_view'),
    path('task/<int:pk>/update/', task_update_view, name='task_update_view'),
    path('task/<int:pk>/delete/', DeleteView.as_view(), name='task_delete_view')
]
