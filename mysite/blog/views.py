from django.shortcuts import render

# Create your views here.
lista_de_posts = {
    "Matheus": "Olá, eu estou estudando para ser um programador web!",
    "Emanuel": "Olá, eu estou estudando para ser um desenvolvedor de jogos!",
    "Hiago": "Olá, eu não estou estudando!"
}


def posts(request):
    return render(request, "posts.html", {})

def post(request, slug):
    nome = slug
    autores = list(lista_de_posts.keys())
    if nome in autores:
        frase = lista_de_posts[nome]
        return render(request, "post.html", { "nome": nome, "frase": frase })
    else: 
        return render(request, "post.html", {"nome": "404", "frase": "Esse autor não existe!"})
        
    
    