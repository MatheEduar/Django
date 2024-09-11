# URLs & Views

Diretório responsável para aprendizado sobre URLs e Views.

## URLs

No Django, as URLs são definidas no arquivo `urls.py`. Este arquivo contém uma lista de padrões de URL que mapeiam para visualizações. 

Um padrão de URL é definido como uma expressão regular que corresponde a uma URL. Quando um usuário solicita uma URL, o Django percorre a lista de padrões de URL definida no arquivo urls.py e encontra o primeiro padrão que corresponde à URL. Se nenhum padrão corresponder, o Django retorna um erro 404.

## Views

Uma vez que o Django encontre um padrão de URL correspondente, ele chama a função de visualização associada no arquivo `views.py`. Uma função de visualização recebe uma solicitação como seu argumento e retorna uma resposta HTTP. A resposta pode ser uma simples mensagem de texto, uma página HTML ou um objeto JSON.