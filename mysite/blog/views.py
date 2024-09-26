from django.shortcuts import render

# Create your views here.
lista_de_posts = {
    "Django": {"img": '/blog/img/django.jpg', "frase": 'Aprendizado em Django'},
    "React-Native": {"img": '', "frase": ''},
    "Sass": {"img": '', "frase": ''}
}

def starting_page(request):
    return render(request, "blog/index.html", {})

def posts(request):
    return render(request, "blog/posts.html", {})

def post_detail(request, slug):
    post = slug
    autores = list(lista_de_posts.keys())
    if post in autores:
        post_info = lista_de_posts[post]
        dict_post_info = dict(post_info)
        frase = dict_post_info["frase"]
        
        return render(request, "blog/post-detail.html", { "nome": post, "post_title": post})
    else: 
        return render(request, "blog/post-detail.html", {"nome": "404", "frase": "Esse autor não existe!"})
        
    
    