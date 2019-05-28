from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from tickets import views as tickets_views

urlpatterns = [
    path('<int:ticket_id>', tickets_views.SingleTicket.as_view()),
    path('new', tickets_views.NewTicket.as_view()),
]
