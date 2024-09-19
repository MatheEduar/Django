# Templates & Static Files

Esse diretório é responsável por conter conteúdo introdutório sobre Templates e Static Files
no framework Django. O código inicial é o mesmo da versão final de `monthly challenges`

## Pasta Templates

* Crie uma pasta chamada `templates` na pasta `challenges`
    * Em seguida crie uma pasta `challenges` na pasta `templates`
        * Crie o arquivo `challenge.html` na pasta `challenges`


## Enviado um html por HttpResponse

* Django utiliza um método para ler um arquivo e transformá-lo em texto
    `from django.template.loader import render_to_string`

* Modifique a view do `views.py` para:

![Screenshot da função `monthly_challenge` modificada](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-0.png)

* Para que a função funcione da maneira devida será necessário configurar o arquivo 
`settings.py`

![Screenshot do arquivo `settings.py` modificado](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-1.png)

* Ou apenas adicionar o `challenges` na lista de `INSTALLED_APPS`, com a configuração
`APP_DIRS` atribuida para `True`

## Função Render

* A função `render` é um atalho para as duas funções responsáveis para enviar a renderização
do arquivo html e enviar a resposta Http, o mesmo código pode ser escrito assim: 

![Screenshot da função render implementada](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-2.png)

## Django Template Language (DTL) 

A sintaxe DTL é utilizada junto com html para poder renderizar as páginas dinamicamente. 

As views irão enviar um dicionário com o variáveis que devem ser acessadas pelo html e seus pares com o conteúdo.

![Screenshot do dicionário colocado para renderização](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-3.png)

Para a página ser renderizada com a variável é necessário utilizar a seguinte sintaxe:

![Screenshot do html modificado](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-4.png)

### Filtros 

* Os filtros são ferramentas poderosas que permitem manipular e formatar dados diretamente nos seus templates HTML. Eles atuam como pequenas funções que recebem um valor e retornam um novo valor modificado, oferecendo flexibilidade para personalizar a exibição de seus dados.


Na versão final `month.capitalize()` é retirado do envio e o filtro `|title` é aplicado ao mês no arquivo html.

### Tags

* As tags são pequenas porções de lógica reutilizável que você insere diretamente em seus templates HTML. Elas permitem que você manipule dados, faça condicionais, inclua outros templates e muito mais, tudo dentro do contexto de sua página. Isso torna seus templates mais dinâmicos e fáceis de manter.


#### For tag

* Modificando a view `index`

![Screenshot da view index modificada](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-5.png)

* Criando o `index.html`

![Screenshot do index.html com a tag for](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-6.png)

* Podemos ver um exemplo da tag for sendo utilizada, essa é a sintaxe utilizada para aplicar a
lógica no front-end da aplicação.

Na versão final a view apenas envia uma lista de meses e o front-end lida com os dados.

#### Url tag

A url tag é um método para utilizar a função `reverse()` no front-end para que não haja problemas voltados a caminhos na aplicação.

![Screenshot da tag url sendo utilizada](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-7.png)

#### If tag

* A tag `if` é uma ferramenta fundamental para controlar o fluxo dos templates, permitindo que a página exiba ou oculte partes do HTML com base em condições específicas.

![Screenshot mostrando a tag if sendo utilizada](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-8.png)

### Herança de Templates

Em Django, a herança de templates é um mecanismo poderoso que permite criar uma estrutura base para seus templates e, em seguida, estender essa estrutura em templates mais específicos. É como criar um modelo para suas páginas, onde você define os elementos comuns a todas elas e depois personaliza cada página individualmente.

* Crie uma pasta `templates` na raiz do projeto, utilizaremos para deixar o html base que será utilizade em todo projeto.

* Crie o arquivo `base.html`, ele será utilizado como uma base html de todo o projeto

![Screenshot do arquivo base.html](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-9.png)

Esse arquivo será utilizado para criar a estrutura html das páginas, utilizando o bloco de título da página e o bloco de conteúdo para deixar os arquivos hmtls mais visíveis.

* Adicione o caminho para o diretório template no `settings.py`. A modificação é necessária para que a tag `extends` nos códigos seguintes consigam acessar o arquivo `base.html`.

![Screenshot da modificação em settings.py](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-11.png)


* Em seguida modifique os arquivos `index.html` e  `challenge.html` para que eles tenham a configuração base do projeto.


#### index.html

![Screenshot do arquivo index.html modificado](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-11.png)

#### challenge.html

![Screenshot do arquivo challenge.html modificado](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-12.png)

### Partials e Snippets

Partials e snippets são recursos que permitem reutilizar fragmentos de código HTML dentro de seus templates Django. Isso ajuda a manter seus templates organizados, mais legíveis e mais fáceis de manter.

* Crie uma pasta chamada partials, ela será responsável por guardar todos os snippets das páginas
relacionadas a aplicação Challenges.

* Crie um arquivo `header.html` e escreva o que deve ser colocado como header nas páginas.

* Utilizando a tag include do django, você poderá incluir o trecho do código em qualquer local utilizando o caminho do arquivo.

#### Exemplo:

    `{% include "challenges/partials/header.html" %}`

## Static Files

Em um projeto Django, arquivos estáticos são aqueles que não mudam dinamicamente, como imagens, folhas de estilo (CSS) e scripts JavaScript. Eles são servidos diretamente para o navegador do usuário, sem a necessidade de processamento pelo servidor Django.

* Para isso, crie uma pasta chamada `static` na aplicação challenges, e para melhorar o uso no projeto, crie outra pasta na pasta `static` chamada challenges

* Adicione os arquivos temporários que precisar, como exemplo utilizaremos o `index.css`

* Adicione um novo bloco no arquivo `base.html`

![Screenshot do arquivo base.html modficado](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-13.png)

* Adicione a tag `{% load static %}` no arquivo `challenge.html` e adicione como conteúdo no arquivo `index.html` nosso caminho para o arquivo `index.css` no bloco criado acima.

![Screenshot do arquivo index.html modificado](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-14.png)

### Arquivos Estáticos Globais

* Adicione uma nova configuração ao arquivo `Settings.py`:

![Screenshot da nova regra adicionada](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-15.png)

* Crie um novo diretório chamado `static` no diretório raiz do projeto e adicione a estilização
geral.

* Adicione o estilo no arquivo `base.html`

![Screenshot do arquivo base.html modificado](https://github.com/MatheEduar/Django/blob/main/monthly_challenges_template/assets/imgs/img-16.png)