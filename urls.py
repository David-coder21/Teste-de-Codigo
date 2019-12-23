from django.contrib import admin 
from django.urls import include, path 

app_name='Empresa' 
urlpatterns = [ 
path(r'', include('Empresa.core.urls') ), 
path(r'', include('Empresa.registration.urls', namespace='registration') ), 
path(r'vagas/', include('Empresa.vacancies.urls', namespace='vacancies') ),
path('admin/', admin.site.urls), ]