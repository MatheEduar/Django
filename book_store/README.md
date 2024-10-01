# Data & Models

Repositório dedicado ao aprendizado sobre Data & Models do framework Django.

## Models.py

O arquivo `models.py` será responsável para criar classes que irão interagir com o Banco de Dados.

As classes devem ter a seguinte configuração:

    `class NomeDaClasse(models.Model):` 

A classe irá herdar uma classe que vem com o Framework Django para facilitar a interação com o Banco de Dados.

As variáveis na classe criada serão responsáveis por associar os tipos de campos que serão preenchidos no banco de dados, elas tem a seguinte configuração:

    `nome_do_campo = models.ConstrutorDoCampoField()`

Basicamente, cada classe será uma tabela no banco de dados.

## Migrations 

Sempre que criamos ou editamos um modelo no `models.py` devemos criar as instruções para que o Django utilize as instruções. Para isso precisamos criar as migrações e executá-las.

Para isso precisaremos rodar o seguinte comando no diretório raíz do projeto:

    `python manage.py makemigrations`

Será criado um arquivo dentro da pasta migrations dos aplicativos utilizados pelo projeto.
Para efetivar a migração devemos rodar o seguinte comando:

    `python manage.py migrate`