"""domotica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from domotica.core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iluminacao/', views.lighting, name='lighting'),
    path('videovigilancia/', views.surveillance, name='surveillance'),
    path('cam01/', views.cam01, name='cam01'),
    path('cliente/', views.clientConnect, name='clientConnect')
]
