from django.shortcuts import render
from .models import Jogador, Time, MeuTime, Jogo

def mostrarJogadores(request):
    mostrar = Jogador.objects.all()
    mostrarTime = Time.objects.all()
    meusTimes = MeuTime.objects.all()
    meusJogos = Jogo.objects.all()
    
    return render(request, 'futebol/jogadores.html', 
                  {'mostrar': mostrar,
                   'mostrarTime': mostrarTime,
                   'meusTimes': meusTimes,
                   'meusJogos': meusJogos,
                   })
