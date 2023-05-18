from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
#selenium e webdrive

options = Options()
options.add_experimental_option("detach", True)

# Passo 1: Entrar na internet (abrir o navegador)
navegador = webdriver.Chrome(options=options)
navegador.get('https://www.google.com')


# Passo 2: Importar a base de dados
tabela = pd.read_excel('Aula3/commodities.xlsx')

for linha in tabela.index:
    produto = tabela.loc[linha, 'Produto']
    produto = produto.replace('ó', 'o').replace('ã', 'a').replace('á', 'a').replace('ç', 'c').replace('ú', 'u').replace('é', 'e')
    # entrar no site melhor cambio
    link = f'https://www.melhorcambio.com/{produto}-hoje'
    print(link)
    navegador.get(link)

    # pegar a cotação do milho
    cotacao = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace('.', '')
    cotacao = cotacao.replace(',', '.')
    cotacao = float(cotacao)
    print(cotacao)

    # .send_keys("escreve no input")
    # .click() clica nele
    # .get_attribute() pega uma informação dele

    # na coluna Preço Atual do Milho, preencher a cotação do milho
    tabela.loc[linha, 'Preço Atual'] = cotacao
tabela['Comprar'] = tabela['Preço Ideal'] > tabela['Preço Atual']
print(tabela)

# Passo 3: Para cada produto da nossa base
# Passo 4: Pegar o preço atual do produto
# Passo 5: Atualizar o preço na base de dados
# Passo 6: Decidir quais produtos a gente vai comprar
# Passo 7: Exportar a base de dados atualizada
navegador.quit()
tabela.to_excel('Aula3/Tabela-atualizada.xlsx', index=False)