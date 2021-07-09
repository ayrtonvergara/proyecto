from django.urls import path
from .views import home,contactanos,form_servicio,inicio,login,quienesSomos,tarjeta1,tarjeta4

urlpatterns = [
    path('',home,name="home"),
    path('contactanos',contactanos,name="contactanos"),
    path('inicio',inicio,name="inicio"),
    path('login',login,name="login"),
    path('quienesSomos',quienesSomos,name="quienesSomos"),
    path('form_servicio',form_servicio,name="form_servicio"),
    path('tarjeta4',tarjeta4,name="tarjeta4"),
    path('tarjeta1',tarjeta1,name="tarjeta1"),
]

