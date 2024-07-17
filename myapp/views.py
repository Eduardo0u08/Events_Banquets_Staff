
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'myapp/index.html')

def registro_view(request):
    return render(request, 'myapp/registro.html')