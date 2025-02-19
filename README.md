# Projeto de Análise de Fluxo de Caixa

Este projeto simula a análise de fluxo de caixa de uma grande organização usando Python, MySQL e Power BI. Ele inclui scripts para gerar dados fictícios, carregar dados no MySQL e criar visualizações interativas no Power BI.

![Dashboard do Power BI](imagens/dashboard.png)

## Estrutura do Projeto

- `gerar_dados.py`: Gera um arquivo CSV com transações financeiras fictícias.
- `carregar_dados.py`: Carrega os dados do CSV para o banco de dados MySQL.
- `conexao.py`: Testa a conexão com o banco de dados MySQL.
- `fluxo_caixa.csv`: Arquivo CSV com os dados fictícios.
- `imagens/`: Screenshots do painel do Power BI.

## Requisitos

- Python 3.x
- MySQL
- Power BI Desktop
- Bibliotecas Python:
  - `pandas`
  - `faker`
  - `mysql-connector-python`