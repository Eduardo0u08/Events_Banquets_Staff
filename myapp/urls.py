
from django.urls import path
from myapp.views import hello_world, registro_view

urlpatterns = [
    path('', hello_world, name='home'),
    path('Registro/', registro_view, name='Registro'),

]

