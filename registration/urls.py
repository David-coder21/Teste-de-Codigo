from django.contrib.auth.views import LoginView
from django.urls import include, path


app_name = 'registration'
urlpatterns = [

    path('', include('django.contrib.auth.urls')),

]