from django.urls import path

from To_Do_list.views import index_view

urlpatterns = [
    path('', index_view)

]
