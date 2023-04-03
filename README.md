# Integração Gabriel
​
## Iniciar a simulação:
Primeiro, é necessário ativar o ambiente virtual do python. Nesse caso, é só executar o seguinte comando no terminal dentro da raiz do projeto:
​
pascoli>Scripts\activate
​
Depois, abrimos o servidor local em flask:
​
pascoli>python app.py
​
## Frontend
O Frontend é composto por uma página com ``divs`` centralizadas com a coordenada atual, um forms para podermos adicionar uma nova coordenada para o robô digital e uma lista com as outras coordenadas do robô digital.
​
## Backend
O backend é composto por rotas em flask que consistem em:
* route('\')
  * Usamos o render_template para servir o index.html na porta padrão da rota
* route('\get_posicao')
  * Retorna para o GODOT um json com a coordenada atual do robô (que é a última coordenada inserida no banco de dados)
* route('\post_posicao')
  * Pega os dados do forms da página e insere no banco de dados, redirecionado para a rota padrão após essa inserção
​
## Banco de dados
O banco de dados e toda a sua estrutura foi criado utilizando o SQLAlchemy. Por isso, tenho a pasta "models" que possui a classe Coordenadas que cria uma tabela no banco de dados. Em cada rota, o banco é acessado pelo "Session" e utilizado para inserir ou selecionar os dados necessários.
​
## Simulação
​
No GODOT o nó Timer faz uma requisição à rota get do backend a cada timeout, com a requisição http completada, a posição do sprite Robozinho é alterada de acordo com as coordenadas obtidas.
