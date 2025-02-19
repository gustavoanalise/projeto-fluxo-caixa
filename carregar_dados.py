import mysql.connector
import csv

# Configuração da conexão com o MySQL
conexao = mysql.connector.connect(
    host="localhost",          
    user="root",        
    password="data321base!",      
    database="fluxo_caixa_db"  
)

cursor = conexao.cursor()

# Ler o arquivo CSV e inserir os dados na tabela
with open('fluxo_caixa.csv', 'r') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        sql = "INSERT INTO transacoes (data, descricao, tipo, valor) VALUES (%s, %s, %s, %s)"
        valores = (linha['data'], linha['descricao'], linha['tipo'], linha['valor'])
        cursor.execute(sql, valores)

# Confirmar as alterações e fechar a conexão
conexao.commit()
cursor.close()
conexao.close()

print("Dados carregados com sucesso!")