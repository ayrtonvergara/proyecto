from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')
def contactanos(request):
    return render(request,'core/contactanos.html')
def form_servicio(request):
    return render(request,'core/form_servicio.html')
def inicio(request):
    return render(request,'core/inicio.html')
def login(request):
    return login(request,'core/login.html')
def quienesSomos(request):
    return render(request,'core/quienesSomos.html')
def tarjeta1(request):
    return render(request,'core/tarjeta1.html')
def tarjeta4(request):
    return render(request,'core/tarjeta4.html')

