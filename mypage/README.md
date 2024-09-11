# Estrutura do Projeto Django.

Diretório responsável para aprendizado de conceitos iniciais do Framework Django.

## Criando Projeto Django.

Após a instalação, para iniciar um projeto em Django execute o comando com essa configuração:
django-admin startproject 'nome do projeto'

```
    django-admin startproject mypage
```
Após a execução do comando uma pasta com a seguinte configuração será criada:

![Screenshot de uma configuração da criação do comando acima.](https://github.com/MatheEduar/Django/blob/main/assets/imgs/mypage/my-page-0.png)

Na pasta teremos o arquivo `manage.py`, o arquivo responsável por gerenciar o projeto Django,
e a pasta **mypage**, que é onde há os outros arquivos do projeto estão armazenados.

## Visualização do Servidor.

Após a criação do projeto, para colocar nosso site no ar devemos escrever os seguintes comandos:

### Para acessar o Projeto:
```
    cd mypage
```

### Para rodar o Server:
```
    python manage.py runserver
```
Esse comando é o que coloca o site no ar. O Framework Django já traz muitas funcionalidades
prontas, como sistema administrativo, sistema de autentificação, sistema de controle de sessões
e cookies, assim por diante.

Depois de executarmos a primeira vez o nosso projeto em Django, também surgirá o banco de dados 
**db.sqlite3** dentro da pasta dele.

![Screenshot de uma configuração do projeto após o comando acima.](https://github.com/MatheEduar/Django/blob/main/assets/imgs/mypage/my-page-1.png)

No terminal que você executou o código será mostrado o endereço do servidor local para que você 
acesse o projeto:

![Screenshot do terminal após comando acima.](https://github.com/MatheEduar/Django/blob/main/assets/imgs/mypage/my-page-2.png)

Adicionando o link em um navegador veremos a seguinte página:

![Screenshot do navegador acessando o endereço disponibilizado pelo terminal.](https://github.com/MatheEduar/Django/blob/main/assets/imgs/mypage/my-page-3.png)

## Estrutura do Projeto Django 

![Sreenshot da estrutura do projeto Django.](https://github.com/MatheEduar/Django/blob/main/assets/imgs/mypage/my-page-1.png)

O projeto terá o arquivo `manage.py` e a pasta com o mesmo nome do projeto.

Nessa pasta, temos o arquivo `__init__.py`, que está vazio. Este arquivo indica
para o Python que essa pasta `mypage` faz parte de um módulo Python.

Os arquivos `asgi.py` e `wsgi.py` são os arquivos de configuração que, quando colocarmos 
o site em um servidor, o servidor saberá como lidar com esse projeto. Utilizaremos esses
arquivos apenas no momento de fazer o **deploy** do projeto.

Além desses arquivos, também temos o `settings.py` e o `urls.py`. No arquivo `urls.py`, é onde definiremos os links, os endereços das páginas do nosso site. Já o `settings.py` é onde iremos de fato configurar o projeto. É dentro desse arquivo que definiremos as configurações e as informações essenciais para o nosso site funcionar corretamente.


# Django Apps

Cada projeto Django terá aplicativos criados dentro dele. Em outras palavras, a estrutura do Django será composta pelo projeto que você criou mais os aplicativos que deseja executar dentro dele.

## Criando App no Django

Para criar um App em Django execute o comando com a seguinte configuração:
python manage.py startapp 'nome do app'

```
    python manage.py startapp challenges
```

Nesse exemplo o App challenges será um App para exemplo para esse repositório.

A configuração do Projeto ficará assim:

![Screenshot da configuração do projeto após o comando acima](https://github.com/MatheEduar/Django/blob/main/assets/imgs/mypage/my-page-4.png)

No arquivo `settings.py` no módulo `mypage`, é necessário declarar o aplicativo que foi criado em
`INSTALLED_APPS`

![Screenshot do INSTALLED_APPS após o passo acima.](https://github.com/MatheEduar/Django/blob/main/assets/imgs/mypage/my-page-5.png)

## Arquivos do App

No App há vários arquivos, um deles é o `__init__.py` que também irá iniciar vazio e indica que 
a pasta `challenges` é um aplicativo do projeto.

A pasta `migrations` é responsável por gerenciar e registrar modificações no banco de dados.

O `admin.py` será onde será configurado o que será exibido na tela de administração do site, ou seja,
o usuário que é administrador do site visualizará ao acessá-lo.

No `apps.py`, será para configurar e registrar os aplicativos referentes à aplicação `challenges`.

O arquivo `tests.py`, serve para executar testes da aplicação.

No `models.py`, é o arquivo onde será definido as informações que serão registradas no seu sistema 
e no seu banco de dados.

O `views.py` é onde será definida a lógica por trás do site, ou seja, onde você definirá as funções 
ou classes que serão executadas quando o usuário acessar um link específico do seu site.