"""helpdesk_ticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Mensajes import views
from tickets import views as tickets_view
from dashboard import views as dashboard_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard_views.get_dashboard),
    path('accounts/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_views.get_dashboard),
    path('Mensajes/', include('Mensajes.urls')),
    path('Tickets/', include('tickets.urls')),
]
