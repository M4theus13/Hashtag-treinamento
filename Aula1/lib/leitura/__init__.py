import pandas as pd

def leitura():
    try:
        # importar a base de dados
        tabela = pd.read_csv(r'C:\Users\mathe\Downloads\Compras.csv', sep=';')
    except:
        print('erro READ')
    else:
        # calculo dos indicadores
        totalGasto = tabela['ValorFinal'].sum() # total gasto
        quantidade = tabela['Quantidade'].sum() # quantidade
        precoMedio = totalGasto / quantidade # preço medio
        
        valor = [totalGasto, quantidade, precoMedio]

        return valor
        

