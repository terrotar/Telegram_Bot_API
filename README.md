
# Escopo


Criar uma API utilizando Django Rest Framework ou Flask em conjunto com uma integração
com Telegram utilizando apenas os métodos  GET e POST. A requisição POST vai receber um JSON,
no qual essas informações serão salvas no banco , após serem salvas será necessário retornar
a informação de acordo com a regra de negócio.

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


# BONUS

- DB: Criar coluna data registro na tabela usuario
    - Foi criado essa nova coluna com o intuito de ser possível realizar um tratamento das tabelas em busca de usuários
registrados há tanto tempo e realizar mensagens para eles com base nesse dado.


- LOG: Integrar .log com biblioteca loguru
    - Com o sistema de log com diversos tipos de níveis(success, error, info) em todas as funcionalidades, comandos
e callbacks/requests, é possível ter uma administração melhor do comportamento do bot. Além disso, é extremamente
mais fácil debuggar o programa caso ele apresente algum tipo de problema. Ainda, é possível obter dados sobre as etapas
que os usuários estão realizando ao interagir com o bot, ficando claro alguns dados que não seriam plausíveis sem os logs
e ainda ao vivo, como a adesão de certo usuário em compartilhar ou não com o bot seu número após iniciar a conversa com o mesmo.


- TEST: Implementar testes unitários com biblioteca pytest
    - Foi desenvolvido alguns testes para a aplicação que apesar de serem simples dão uma segurança e estabilidade maior
para qualquer aplicação. Ainda possui uma escalabilidade absurda, sendo muito prático de incrementar mais testes futuramente. Foi desenvolvido com foco na Blueprint api pois a própria estrutura de commands e handlers do bot localizado em app/telegram/telebot.py
já contorna, controla e evita diversos tipos de erros.


# Como Inicicar

- Instalar bibliotecas do Pipfile(similar ao requirements.txt)

- Abrir um terminal e entrar na pasta do pacote 'app'

- iniciar o flask com o parametro '--no-reload' pois por estar com debug=True e ambiente(env) Development, ele inicia duas vezes
a aplicação para ter a função de atualizar com modificações sem cair do ar, gerando um conflito de HttpRequests caso rode simplesmente
com o 'flask run'.

<code>flask run --no-reload</code>


- Chame o bot @Terrotar_GitWebDevTestBot para iniciar a conversa.

- Acesse as URL's da API para poder utilizar o sistema no navegador.
URL's:
- localhost/api/all_users: Disponibiliza todos usuários cadastrados no banco de dados.
- localhost/api/user/get/<id_user>: Substitua <id_user> pelo id do usuário que deseja coletar informações dentro do banco de dados.
- /user/message/<user_id>/<message>: Substitua <user_id> pelo id do usuário e <message> pela mensagem que deseja enviar via POST para
o usuário.

Obs1: Dentro dessa última route é realizado o envio do post através de um JSON com auxílio da biblioteca 'requests'. Para mais infos, veja app/blueprints/api/routes.py.

Obs2: Caso ao rodar o comando flask retorne um erro do 'sqlite3 OperationalError: unable to open database file' verifique se a pasta app/database está criada e seu arquivo app/database/sqlite.db.

Obs3: Para rodar os testes, basta abrir um terminal e ir na pasta /tests e digitar o comando <code>pytest</code>. Certifique-se de que a aplicação está rodando, ou todos testes irão falhar ao tentar conectar com as URL's.


# Sobre

    Esse projeto foi bem difícil, principalmente no começo por nunca ter utilizado o Telegram. Fiquei impressionado com o aplicativo
e suas funcionalidades, mas demorei um pouco para entender como ele funcionava e seus bots também. Para desenvolver levei um bom tempo
para assimilar a parte de estrutura de comamandos e handlers, como eles se interagiam e se comportavam com a interação com usuário. É
incrível como os bots do Telegram são intuitivos para se utilizar, é possível literalmente guiar o usuário para caminhos através dos comandos, evitando assim alguns casos de erros e garantindo o fluxo desejado de etapas.

   Todas as etapas e funções geram um log localizado na pasta app/logs e também no terminal q o bot está rodando, auxiliando o acompanhamento do bot e usuário, como novo usuário se cadastra é gerado um success log e caso ele tente em seguida se cadastrar novamente é gerado um error log. Os logs são descritivos no formato JSON seguindo a ideia da aplicação e buscando ser objetivo e informativo para análises.

    Para coletar o contato do usuário com o seu celular foi criado alguns botões e foi optado por não serem Inline, devido a praticidade
dos padrões KeyBoardButtons de terem como um de seus atributos opcionais o "request_contact". Caso o usuário compartilhe seu contato,
um "messageHandler" irá reconhecer esse tipo de dado e adiciona na tabela 'usuario' caso o mesmo já não esteja adicionado.

    Para realizar as manipulações do banco de dados dentro da lógica do bot foi necessário criar uma conexão/cursor, localizado em app/telegram/dbhelper.py para facilitar a leitura, desenvolvimento e compreensão das funções, como add_user por exemplo. Na Blueprint api não foi necessário pois o flask reconhece automaticamente o banco de dados caso tenha algum comando dele dentro das routes do próprio Flask, o que não é possível no código do bot(app/telegram/telebot.py) e por isso a decisão de um 'DbHelper'.

    Para disponibilizar os dados em formato JSON, foi utilizado a biblioteca marshmallow, gerando assim os 'dumps' e 'loads' necessários para tal.

    A arquitetura do projeto foi desenvolvida em 'Factory Pattern', um conceito estrutural que conheci há pouco tempo e que facilitou muito meus projetos com Flask. Além disso, evitou de mais bug's relacionados com circular imports, deixando o código mais limpo e organizado também. Ainda foi comentado todo o projeto, tentando buscar uma explicação mais fácil caso alguem leia seu código.

    De uma maneira geral, o bot funciona muito bem apesar de ser bem simples. Gostaria de poder me aprofundar mais, fazer o bot responder com stickers e outras interações, dar um pouco mais de 'vida' para ele mas pela minha dificuldade em não conhecer previamente o Telegram e como os bots funcionam, foquei na sua funcionalidade primeiro. Outro ponto que gostaria de ter impementado mas não consegui há tempo foi desenvolver algum sistema, nem que fosse muito pequeno, de chat caso o usuário digitasse algo comum, como um 'Oi' ou algo parecido. Gostaria também de ter implementado o docker mas ainda estou estudando e preciso de mais tempo para poder começar integrar seus conceitos nos meus projetos.

    Apesar desses desejos não realizados no projeto, acredito que ele foi bem realizado e gostei muito de ter criado meu primeiro bot, aprendi muito com o desenvolvimento dele e certamente irei fazer mais bots e utilizar o Telegram. Há diversas vantagens em se utilizar o Telegram e a questão da quantidade e objetivo dos milhares de bots q ele possui que é quase impossível você não aderir a essa ferramenta.
