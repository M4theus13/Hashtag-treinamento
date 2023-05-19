import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Passo 1: Entendimento do Desafio
# Passo 2: Entendimento da Área/Empresa
# Passo 3: Extração/Obtenção de Dados
tabela = pd.read_csv('Aula4/barcos_ref.csv')
print('-='*40)
print(f'{"Tabela de Barcos":^80}')
print('-='*40)

print(tabela)

# Passo 4: Ajuste de Dados (Tratamento/Limpeza)

# Passo 5: Análise Exploratória
print('-='*40)
print(f'{"Correlação entre Preço e Características do Barco":^80}')
print('-='*40)

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

print('-='*40)

print(f'Porcentagem de acerto IA Regressão Linear: {r2_score(yTeste, prevRL):.2f}%') # score regressão linear
print(f'Porcentagem de acerto IA Árvore de Decisão: {r2_score(yTeste, prevAD):.2f}%') # score árvore decisão

# Passo 7: Interpretação de Resultados
print('-='*40)
print(f'{"Tabela Novos Barcos":^80}')
print('-='*40)

tabelaNova = pd.read_csv('Aula4/novos_barcos.csv')
print(tabelaNova)
previsao = modeloArvoreDecisao.predict(tabelaNova)

print('-='*40)

for c, i in enumerate(previsao):
    print(f'Estimativa de preço barco {c} = R$ {i:.2f}')
print('-='*40)
