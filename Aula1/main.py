import pyautogui
from time import sleep
from lib.leitura import *
from lib.email import *

pyautogui.PAUSE = 1

# Passo 1: Acessar o sistema da empresa
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('Enter')
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('Enter')

sleep(2)

# Passo 2: Fazer o login no sistema
pyautogui.click(x=668, y=349) # click input login
pyautogui.write('Meu login')

pyautogui.click(x=655, y=442) # click input senha
pyautogui.write('Minha senha')

pyautogui.click(x=657, y=498)

sleep(3)

# Passo 3: Baixar a base de dados
pyautogui.click(x=478, y=324)
pyautogui.click(x=630, y=619)

sleep(2)

# Passo 4: Calcular os indicadores
leitura()

# Passo 5: Enviar o email para a diretoria/para o chefe
enviar()