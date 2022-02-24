from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import (RegisterView,
                            UserProfileView,
                            UserList,
                            UpdateUserView,
                            UserPasswordChangeView)

app_name = 'accounts'

urlpatterns = [
    path("<int:pk>/", UserProfileView.as_view(), name="user_profile"),
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegisterView.as_view(), name="registration"),
    path("profile/list", UserList.as_view(), name="profile_list"),
    path("<int:pk>/update/", UpdateUserView.as_view(), name="update_user"),
    path("change_password/", UserPasswordChangeView.as_view(), name="change_password")
]
