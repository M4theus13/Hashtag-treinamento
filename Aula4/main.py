import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Passo 1: Entendimento do Desafio
# Passo 2: Entendimento da Área/Empresa
# Passo 3: Extração/Obtenção de Dados
tabela = pd.read_csv('Aula4/barcos_ref.csv')
print(tabela)

# Passo 4: Ajuste de Dados (Tratamento/Limpeza)
print(tabela.info())

# Passo 5: Análise Exploratória
print(tabela.corr()['Preco']) # mostra a correlação da tabela

# Passo 6: Modelagem + Algoritimos(IA)
# Preparação
# separar a base de dados de X e Y
y = tabela['Preco']
x = tabela.drop('Preco', axis=1)

xTreino, xTeste, yTreino, yTeste = train_test_split(x, y, test_size=0.3)

# Criação e Treino da IA
# importar a IA
# criar a IA
modeloRegressaoLinear = LinearRegression()
modeloArvoreDecisao = RandomForestRegressor()

# treinar a IA
modeloRegressaoLinear.fit(xTreino, yTreino) # treino IA regressão linear
modeloArvoreDecisao.fit(xTreino, yTreino) # treino IA árvore decisão

prevRL = modeloRegressaoLinear.predict(xTeste)
prevAD = modeloArvoreDecisao.predict(xTeste)

print(r2_score(yTeste, prevRL)) # score regressão linear
print(r2_score(yTeste, prevAD)) # score árvore decisão

# Passo 7: Interpretação de Resultados
tabelaNova = pd.read_csv('Aula4/novos_barcos.csv')
print(tabelaNova)
previsao = modeloArvoreDecisao.predict(tabelaNova)
print(previsao)
