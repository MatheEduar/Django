from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None #"Desafio: Revisitar seu mural de sonhos e metas e avaliar o que você conquistou.",
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        text_challenge = monthly_challenges[month] 
        return render(request, "challenges/challenge.html", 
            {
                "text": text_challenge,
                "month": month
            })
    except:
        response_data = render_to_string("404_error.html")
        return HttpResponse(response_data)

