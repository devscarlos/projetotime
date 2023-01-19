from django.contrib import admin
from .models import Jogador, Time, MeuTime, Jogo

class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_inicial')
    search_fields = ('nome',) #busca no banco
    list_per_page = 5
    model = Jogador
    
    
class JogoAdmin(admin.ModelAdmin):
    list_display = ('timeA','timeA_gol', 'timeB_gol','timeB')
    model = Jogo
    
    
admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Time)
admin.site.register(MeuTime)
admin.site.register(Jogo, JogoAdmin)

