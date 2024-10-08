from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Desafio: Criar um mural de sonhos e metas para o ano.",
    "february": "Desafio: Ler um livro de autoajuda ou desenvolvimento pessoal.",
    "march": "Desafio: Incorporar uma nova fruta ou legume na sua dieta diária.",
    "april": "Desafio: Tentar uma nova atividade artística, como pintura, desenho ou escrita criativa.",
    "may": "Desafio: Dedicar 30 minutos por dia para meditar ou praticar yoga.",
    "june": "Desafio: Visitar um parque ou área verde pelo menos uma vez por semana.",
    "july": "Desafio: Aprender uma nova habilidade, como tocar um instrumento ou falar um novo idioma.",
    "august": "Desafio: Fazer um passeio diferente, como camping, trilhas ou visitar uma cidade próxima.",
    "september": "Desafio: Organizar um espaço da sua casa que esteja bagunçado.",
    "october": "Desafio: Escrever três coisas pelas quais você é grato todos os dias.>",
    "november": "Desafio: Fazer um trabalho voluntário ou doar para uma causa que você acredita.",
    "december": "Desafio: Revisitar seu mural de sonhos e metas e avaliar o que você conquistou.",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"
        response_data = f"<ul>{list_items}</ul>"
    
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        text_challenge = monthly_challenges[month] 
        response_data = f"<h1>{text_challenge}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponse("Esse mês não existe!")

