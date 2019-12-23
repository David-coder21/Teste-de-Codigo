from django.urls import path, include
from Empresa.core import views 
urlpatterns = [ 
    path(r'', views.home, name='home'), 
    path(r'Empresas/', views.contact, name='contact'), 
    path('registrar/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    ]