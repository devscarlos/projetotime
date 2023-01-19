from django.urls import path
from .views import mostrarJogadores

urlpatterns = [
    path('mostrar', mostrarJogadores),
]