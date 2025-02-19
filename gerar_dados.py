import pandas as pd
from faker import Faker
import random
from datetime import timedelta, datetime

# Configurações iniciais
NUM_TRANSACOES = 10000  # Número de transações a serem geradas
DATA_INICIAL = datetime(2022, 1, 1)  # Data inicial das transações
DATA_FINAL = datetime(2023, 12, 31)  # Data final das transações

# Inicializar o gerador de dados fictícios
fake = Faker()

# Função para gerar uma data aleatória dentro do intervalo
def gerar_data_aleatoria():
    delta = DATA_FINAL - DATA_INICIAL
    random_days = random.randint(0, delta.days)
    return DATA_INICIAL + timedelta(days=random_days)

# Função para gerar descrições fictícias
def gerar_descricao(tipo):
    if tipo == "receita":
        descricoes = ["Salário", "Venda de produto", "Reembolso", "Investimento"]
    else:
        descricoes = ["Aluguel", "Conta de luz", "Compra de estoque", "Manutenção"]
    return random.choice(descricoes)

# Gerar dados fictícios
dados = []
for _ in range(NUM_TRANSACOES):
    tipo = random.choice(["receita", "despesa"])
    valor = round(random.uniform(100, 10000), 2)  # Valores entre 100 e 10.000
    if tipo == "despesa":
        valor = -valor  # Transformar em negativo para despesas
    dados.append({
        "data": gerar_data_aleatoria(),
        "descricao": gerar_descricao(tipo),
        "tipo": tipo,
        "valor": valor
    })

# Criar DataFrame com os dados
df = pd.DataFrame(dados)

# Salvar os dados em um arquivo CSV
df.to_csv("fluxo_caixa.csv", index=False)

print(f"Arquivo 'fluxo_caixa.csv' gerado com {NUM_TRANSACOES} transações.")