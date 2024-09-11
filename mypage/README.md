# Estrutura do Projeto Django.

## Criando Projeto Django.

Após a instalação, para iniciar um projeto em Django execute o comando com essa configuração:

django-admin startproject 'nome do projeto'

```
    django-admin startproject mypage
```
Após a execução do comando uma pasta com a seguinte configuração será criada:

![Screenshot de uma configuração da criação do comando acima.](../assets/imgs/mypage/image_mypage.png)

Na pasta teremos o arquivo **manage.py**, o arquivo responsável por gerenciar o projeto Django,
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

![Screenshot de uma configuração do projeto após o comando acima.](../assets/imgs/mypage/my-page-1.png)

No terminal que você executou o código será mostrado o endereço do servidor local para que você 
acesse o projeto:

![Screenshot do terminal após comando acima.](../assets/imgs/mypage/my-page-2.png)

Adicionando o link em um navegador veremos a seguinte página:

![Screenshot do navegador acessando o endereço disponibilizado pelo terminal.](../assets/imgs/mypage/my-page-3.png)

