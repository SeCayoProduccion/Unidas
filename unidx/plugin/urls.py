from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('busqueda/', views.busqueda, name='busqueda'), 
    path('negocio/', views.negocio, name='negocio'),
    path('visitantes/', views.visitantes, name='visitantes')
    
]
