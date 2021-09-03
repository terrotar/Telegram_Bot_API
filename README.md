
# Escopo

Boa tarde!!

Segue o desafio como combinado. 


Criar uma API utilizando Django Rest Framework ou Flask em conjunto com uma integração
com Telegram utilizando apenas os métodos  GET e POST. A requisição POST vai receber um JSON,
no qual essas informações serão salvas no banco , após serem salvas será necessário retornar
a informação de acordo com a regra de negócio


Primeiro passo: Criar um projeto Django Rest Framework ou Flask;
OK



Segundo passo: Fazer a integração com o Telegram juntamente com as devidas permissões do mesmo;
OBS 1: Existem diversos vídeos no youtube mostrando como integrar com o Telegram.
OK



Terceiro passo: Após confirmar a aceitação do usuário no Telegram,
salvar essas informações do usuário no banco de dados;
OK




Quarto passo: Criar a API com dois tipos de métodos HTTP, GET e POST,
no qual o GET trará as informações dos usuários, que aceitaram a integração do Telegram
e o POST enviará uma mensagem para o número do usuário selecionado no GET;
OBS 2: O JSON que será enviado é livre desde que tenha a key “text” que será a
mensagem enviada para o número de celular do usuário. Esses dados do JSON que serão enviados
pelo método POST, além de serem enviados para o usuário, deverão ser salvos no banco de dados.
OK




Ferramentas: Django, Django Rest Framework ou Flask.
Bancos relacionais que poderão ser utilizados: SQLite3 , Postgres ou MySQL.
OBS 3: Será considerado um plus a utilização de ferramentas como Docker, RabbitMQ e Celery
OBS: link do github após terminar
JSON example:

{
“text”: “mensage”,

"nome": "nome",
“cel_number” : 55999999999,
“id”: 1
}


# BONUS

- DB
Criar coluna data registro na tabela usuario
Integrar coluna registro da tabela usuário com tabela mensagem


- LOG
Integrar .log por dia


- TEST
Implementar testes unitários


- BOT
Opção de descadastrar do sistema via chat
Utilizar stickers com os callbacks do bot
Melhorar descrição do bot
