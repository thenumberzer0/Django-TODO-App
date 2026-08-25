from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("upload/", views.upload_tasks, name="upload_task"),
    path("task/<int:pk>/toggle/", views.toggle_task, name="toggle_task"),
    path("task/<int:pk>/delete/", views.delete_task, name="delete_task"),
]
