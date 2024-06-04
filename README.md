# Projeto API NBA

Esta é uma API simples construída com Flask que retorna (em JSON) dados fictícios dos resultados dos jogos da NBA.
Foi um desafio proposto na faculdade com o objetivo de implementar uma esteira CI/CD, contendo os estágios Build, Test e Deploy.

## Instalação

1. Clone o repositório:
   
   ```sh
   git clone #repositório do github

2. Entre no diretório do projeto:
   
   ```sh
   cd esteira_cicd_nba_api

## Ambiente Virtual
3. Crie e ative um ambiente virtual:
   
   ```sh
   python -m venv .venv
   source .venv/bin/activate # No Windows use `venv\Scripts\activate`

## Dependências: 
4. Instale as dependências:
   
   ```sh
   pip install -r requirements.txt

## Executando aplicação: 
5. Rodar aplicação
   
   ```sh
   python app/app.py

## Testar API no navegador
http://127.0.01:5003/

## Acessar os dados da Api em JSON
http://127.0.01:5003/v1/resultados_nba