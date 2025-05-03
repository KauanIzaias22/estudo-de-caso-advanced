# Projeto Streamlit + MongoDB com Docker

## Introdução

Este projeto foi desenvolvido para demonstrar a criação de um ambiente isolado e padronizado usando Docker, integrando uma aplicação em Streamlit com um banco de dados MongoDB.  
O foco é realizar operações básicas como inserção, manipulação, concatenação e leitura de dados.

## Objetivos do projeto

- Utilizar Docker para gerenciar a infraestrutura e garantir a portabilidade do ambiente.
- Configurar um container MongoDB acessível para a aplicação.
- Desenvolver uma aplicação simples em Streamlit (`app.py`) que conecta ao MongoDB e executa operações básicas no banco de dados.

## Descrição do Projeto

### Docker

O Docker é utilizado para:
- Subir um container MongoDB pré-configurado.
- Garantir que o ambiente da aplicação seja idêntico em qualquer máquina.
- Facilitar o gerenciamento e a escalabilidade.

### MongoDB

O MongoDB roda dentro de um container e armazena os dados manipulados pela aplicação.  
Ele é configurado no arquivo `docker-compose.yml`, incluindo:
- Nome do serviço.
- Porta exposta.
- Volume para persistência dos dados.

### Streamlit (`app.py`)

O app em Streamlit:
- Conecta-se ao MongoDB.
- Realiza inserção, leitura, concatenação e manipulação de dados.
- Apresenta os resultados diretamente na interface web.
from pymongo import MongoClient

# Conexão com o MongoDB (ajuste a URI conforme o docker-compose)
client = MongoClient('mongodb://mongo:27017/')  # 'mongo' é o nome do serviço no docker-compose
db = client['meu_banco']  # Nome do banco de dados
collection = db['minha_colecao']  # Nome da coleção (tabela)

