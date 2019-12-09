# APP-Campus-Online-v4.0
Repositório para o desenvolvimento da quarta versão do App do Campus Multiplataforma (2019/2).

Dúvidas gerais em relação ao processo de desenvolvimento, consulte a [Documentação Oficial do Django](https://docs.djangoproject.com/pt-br/2.2/), que foi utilizada amplamente nesta aplicação. A versão utilizada foi a Django 2.2.

Em caso de dúvidas relacionado a este projeto, você pode contatar os desenvolvedores da v4.0 pelo GitHub: [fernandams](https://github.com/fernandams) e [jlyamin](https://github.com/jlyamin).

## Environment
Para o desenvolvimento do aplicativo é necessário um ambiente virtual do Python.

Virtualenv é um ambiente virtual do python que permite instalar bibliotecas para cada aplicação isoladas da máquina.

Em relação ao git, o env fica no .gitignore

Depois de clonado o repositório, é necessário criar um env (virtualenv), ativá-lo e instalar o que for necessário, seguem os comandos:

1. virtualenv -p python3 env (comando para criar um virtualenv)
2. source env/bin/activate (comando para ativar o env)
* Sempre que for instalar algo ou executar a aplicação é necessário usar esse comando para ativar o ambiente
* Se quiser sair do ambiente basta digitar: deactivate
3. pip install -r requirements.txt (comando para instalar os requisitos do env do projeto, django por exemplo)
* É possível utilizar esse 3º comando visto que o comando pip freeze mostra tudo que está instalado no env, e o seguinte comando:
* pip freeze > requirements.txt 
* grava nesse arquivo txt o que está instalado. 

## Sistema de Pastas
    Este projeto é divido em dois apps do Django, accounts e campus_app. 
    A pasta accounts é onde se encontram os templates, views, models e toda estrutura referente às contas de usuário e lógica relativa a autenticação. 
    Enquanto na pasta campus_app está a estrutura de notícias, página inicial, backoffice, etc.
    Todo o estilo do aplicativo está definido no arquivo styles.scss, no diretório campus_app/static/styles.scss. O arquivo com o estilo antigo do aplicativo está em campus_app/static/css/original.scss (Não recomendo que retorne à versão antiga).

## Seeds
    Existem dois arquivos de seeds principais nesta versão do repositório. A primeira delas está em accounts/fixtures, e existe para criar os grupos de usuário e suas respectivas permissões (Editor e Repórter). Essas permissões podem ser visualizadas no painel de admin do Django.
    A segunda é uma cópia do estado do banco de dados do App em 2019/2. Foi utilizado para ter uma base de testes similar a real.
    Para gerar uma cópia do banco de dados, é necessário, no console do servidor em produção, dentro do virtual enviroment, rodar o comando python manage.py dumpdata > db.json.
    Tendo o arquivo das seeds na raiz do projeto, basta executar python manage.py loaddata db.json para efetivar as mudanças.
    Foi gerada uma base de dados 