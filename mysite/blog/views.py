from django.shortcuts import render

# Create your views here.
lista_de_posts = {
    "Matheus": "Olá, eu estou estudando para ser um programador web!",
    "Emanuel": "Olá, eu estou estudando para ser um desenvolvedor de jogos!",
    "Hiago": "Olá, eu não estou estudando!"
}

def starting_page(request):
    return render(request, "blog/index.html", {})

def posts(request):
    return render(request, "blog/posts.html", {})

def post_detail(request, slug):
    nome = slug
    autores = list(lista_de_posts.keys())
    if nome in autores:
        frase = lista_de_posts[nome]
        return render(request, "blog/post.html", { "nome": nome, "frase": frase })
    else: 
        return render(request, "blog/post.html", {"nome": "404", "frase": "Esse autor não existe!"})
        
    
    