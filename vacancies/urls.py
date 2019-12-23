from django.urls import path 
from Empresa.vacancies import views 

app_name= 'index'
urlpatterns = [ 
    path(r'', views.index, name='index'),
    path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'), 
    
    
    ]