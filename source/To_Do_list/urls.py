from django.urls import path

from To_Do_list.views import (
    IndexView,
    One_Task_View,
    TasksView,
    AddView,
    ProjectCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectTaskAdd,
    TaskUpdateView,
    TaskDeleteView, ProjectUpdateView, ProjectDeleteView, ProjectParticipantAdd, ProjectParticipantDelete,
)
app_name = 'To_Do_list'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('new_task/', AddView.as_view(), name='add_task_view'),
    path('view_tasks/', TasksView.as_view(), name='view_tasks_view'),
    path('task/<int:pk>/', One_Task_View.as_view(), name='one_task_view'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update_view'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete_view'),
    path('new_project/', ProjectCreateView.as_view(), name='create_project_view'),
    path('view_projects/', ProjectListView.as_view(), name='projects_view'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_view'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update_view'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete_view'),
    path('project/<int:pk>/new_task/', ProjectTaskAdd.as_view(), name='task_project_view'),
    path('project/<int:pk>/participant/add/', ProjectParticipantAdd.as_view(), name='participant_add'),
    path('project/<int:pk>/participant/delete', ProjectParticipantDelete.as_view(), name="participant_remove")
]
