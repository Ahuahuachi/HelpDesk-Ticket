from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from user import views as usr_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('register/', usr_views.Register.as_view()),
]
