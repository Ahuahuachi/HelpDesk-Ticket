from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Mensajes import views
from tickets import views as tickets_views

urlpatterns = [
    path('', views.get_MensajeEntrada),
    path('Leer_Mensajes/', views.get_Mensaje),
    path('Tickets/<int:ticket_id>', tickets_views.SingleTicket),
    path('Nuevo_Mensaje/', views.create_Mensaje),
    path('Chat_Mensaje/', views.get_Chat)
]
