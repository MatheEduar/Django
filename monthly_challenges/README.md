# URLs & Views

Diretório responsável para aprendizado sobre URLs e Views.

## URLs

No Django, as URLs são definidas no arquivo `urls.py`. Este arquivo contém uma lista de padrões de URL que mapeiam para visualizações. 

Um padrão de URL é definido como uma expressão regular que corresponde a uma URL. Quando um usuário solicita uma URL, o Django percorre a lista de padrões de URL definida no arquivo urls.py e encontra o primeiro padrão que corresponde à URL. Se nenhum padrão corresponder, o Django retorna um erro 404.

## Views

Uma vez que o Django encontre um padrão de URL correspondente, ele chama a função de visualização associada no arquivo `views.py`. Uma função de visualização recebe uma solicitação como seu argumento e retorna uma resposta HTTP. A resposta pode ser uma simples mensagem de texto, uma página HTML ou um objeto JSON.


# Criando o app Monthy Challenges

## Crie o projeto
`django-admin startproject monthly_challenges`

## Crie um novo app 
`python manage.py startapp challenges`

Modifique o arquivo `views.py` para:

![Screenshot do views.py modificado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-0.png)

Crie um novo arquivo chamado `urls.py` no app challenges

`touch challenges/urls.py`

E modifique-o para ficar assim:

![Screenshot do views.py modificado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-1.png)

`from django.urls import path`

* Importa a função `path` do módulo `django.urls`. Esta função é usada para criar padrões de URL.

`from . import views`

* Importa o módulo views do mesmo diretório. É nesse módulo que as funções que serão chamadas quando uma URL for acessada estão.

`urlpatterns = [ ... ]`

* Cria uma lista chamada `urlpatterns` para armazenar os padrões de URL. Essa lista é essencial para
o Django saber como lidar com as diferentes URLs do site.

`path("january", views.index)`

* Define um padrão de url
    * `"january"`: é a parte da URL que será comparada com as solicitações. Se alguém digitar `/january` no navegador, essa parte da URL corresponderá a esse padrão.
    * `views.index`: É a função que será chamada quando a URL corresponder ao padrão. A função
    `index` provavelmente está definida no módulo `views` e é responsável por gerar a página 
    para a seção "janeiro" do site.

Modifique o arquivo `urls.py` no diretório `monthly_challenges` para que fique assim:
![Screenshot do arquivo monthly_challenges/urls.py modificado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-2.png)

`from django.urls import path, *include*`

* Inclui os padrões de URL de outro arquivo

`path("challenges/", include("challenges.urls"))`

* `'challenges/'`: Qualquer URL que começar com '/challenges/' será direcionada para aqui.

* `include('challenges.urls')`: Inclui os padrões de URL definidos no arquivo que está no aplicativo
`challenges` chamado `urls.py`

### Pesquisando a url `localhost:8000/challenges/january` no nosso navegador teremos:

![Screenshot do navegado com o link acima](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-3.png)


## Aprimorando o Site

### Modifique o arquivo `views.py` para:

![Screenshot do arquivo modificado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-4.png)


### Modifique o arquivo ´urls.py´ do módulo ´challenges´

![Screenshot do arquivo modificado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-5.png)

* `HttpResponseNotFound` é o tipo de resposta que permite o Django enviar um erro 404 Not Found.
* `def monthly_challenge(request, month)` o parâmetro month deve ser igual ao argumento que estará 
entre `<>` no arquivo `urls.py` para que possa ser trabalhada como variável na função.

## Aprimorando o Site para aceitar Inteiros e Strings

### Modifique o arquivo ´urls.py´

![Screnshot do arquivo urls modificado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-6.png)

* A alteração permite que as funções no `views.py` possam ser acessadas de duas formas diferentes com
o mesmo nome da variável, mas com tipos diferentes.

### Redirecionando com dados tratados em `views.py`

Adicione a função `HttpResponseRedirect` do módulo `django.http`

![Screenshot do arquivo `views.py modificado`](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-7.png)

* A função `monthly_challenge_by_number` é responsável por:
    1. Pegar todas as chaves do dicionário `monthly_challenges` e converter para uma lista.
    2. Modificar o valor do mês para que possa acessar a lista de maneira correta.
    3. Redireciona para a rota `monthly_challenge`

## Reverse Function & Named URLs

Para que o código seja consistente e sustentável, alguns trechos do código devem mudar, para que 
quando mudarmos as variáveis, trechos diferentes do código não quebrem. 

O exemplo do curso é dado pela mudança do path em `monthly_challenges/urls.py`, a simples mudança
de `challenges` para `challenge` quebra o acesso ao site, e trás inconsistências ao código, já que
a função de redirecionamento em `/challenges/views.py` redirecionará o cliente para uma página que
não existiria.

### Resolvendo o Problema

Modifique o arquivo `urls.py`

![Screenshot do arquivo `/challenges/urls.py` modificado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-8.png)

* A variável `name` poderá ser utilizada para construir caminhos para apontar para a URL

Adicione o trecho de código no arquivo `views.py`:

`from django-urls import reverse`

Em seguida modifique a função de redirecionamento para: 

![Screenshot do arquivo modificado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-9.png)

## Completando o Site

### Adicionando path para o index

Adicione um path ao arquivo `urls.py`

![Screenshot do arquivo urls.py finalizado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-10.png)

Adicione uma view ao arquivo `views.py`

![Screenshot do arquivo views.py finalizado](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-11.png)

* O código cria uma lista html com links para os meses no calendário do dicionário do código e envia
como resposta final para o usuário.

![Screenshot do index do site](https://github.com/MatheEduar/Django/blob/main/assets/imgs/monthly_challenges/monthly_challenges-12.png)