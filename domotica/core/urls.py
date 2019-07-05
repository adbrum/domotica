from django.urls import path

from domotica.core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iluminacao/', views.lighting, name='lighting'),
    path('videovigilancia/', views.surveillance, name='surveillance'),
    path('cam01/', views.cam01, name='cam01'),
    path('cliente/', views.clientConnect, name='clientConnect'),
    path('estores/', views.blindPosition, name='blindPosition')
]
