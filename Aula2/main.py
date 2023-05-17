import pandas as pd
import plotly.express as px


# Passo 1: Pegar/Importar a base de dados
tabela = pd.read_csv("Aula2/clientes.csv", encoding='latin', sep=';')
# axis = 0 para deletar linha, axis = 1 para deletar coluna
tabela = tabela.drop('Unnamed: 8',axis=1)

# Passo 2: Visualizar a base de dados
    # Entender as informações que você tem disponíveis
    # Procurar os problemas da base de dados
# print(tabela)

# Passo 3: Tratamento de Dados
tabela['Salário Anual (R$)'] = pd.to_numeric(tabela['Salário Anual (R$)'], errors='coerce') # converte o salario de string para num

tabela = tabela.dropna() # todas linhas com valores vazios são removidas
# print(tabela.info()) # mostra as informações da tabela

# Passo 4: Análise Inicial = entender como estão as notas dos clientes
# print(tabela.describe())

# Passo 5: Análise Completa = traçar o perfil ideal de cliente = entender como cada características do cliente impacta na nota
for coluna in tabela.columns:
    if coluna != 'Nota (1-100)' and coluna != 'ClienteID' and coluna != 'Origem':
        grafico = px.histogram(tabela, x =coluna, y='Nota (1-100)', histfunc='avg',text_auto=True, nbins=20) # cria o gáfico

        grafico.show() # exibe o grafico