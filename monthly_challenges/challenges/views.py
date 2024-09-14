from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge(request, month):
    if month == 'january':
        return HttpResponse("<h1>Desafio: Criar um mural de sonhos e metas para o ano.</h1>")
    elif month == 'february':
        return HttpResponse("<h1>Desafio: Ler um livro de autoajuda ou desenvolvimento pessoal.</h1>")    
    elif month == 'march':
        return HttpResponse("<h1>Desafio: Incorporar uma nova fruta ou legume na sua dieta diária.</h1>")
    elif month == 'april':
        return HttpResponse("<h1>Desafio: Tentar uma nova atividade artística, como pintura, desenho ou escrita criativa.</h1>")    
    elif month == 'may':
        return HttpResponse("<h1>Desafio: Dedicar 30 minutos por dia para meditar ou praticar yoga.</h1>")
    elif month == 'june':
        return HttpResponse("<h1>Desafio: Visitar um parque ou área verde pelo menos uma vez por semana.</h1>")    
    elif month == 'july':
        return HttpResponse("<h1>Desafio: Aprender uma nova habilidade, como tocar um instrumento ou falar um novo idioma.</h1>")
    elif month == 'august':
        return HttpResponse("<h1>Desafio: Fazer um passeio diferente, como camping, trilhas ou visitar uma cidade próxima.</h1>")    
    elif month == 'september':
        return HttpResponse("<h1>Desafio: Organizar um espaço da sua casa que esteja bagunçado.</h1>")
    elif month == 'october':
        return HttpResponse("<h1>Desafio: Escrever três coisas pelas quais você é grato todos os dias.</h1>")
    elif month == 'november':
        return HttpResponse("<h1>Desafio: Fazer um trabalho voluntário ou doar para uma causa que você acredita.</h1>")
    elif month == 'december':
        return HttpResponse("<h1>Desafio: Revisitar seu mural de sonhos e metas e avaliar o que você conquistou.</h1>")
    else:
        return HttpResponseNotFound("Esse mês não existe!")
    