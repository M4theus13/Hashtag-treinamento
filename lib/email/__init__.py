import pyautogui
from time import sleep
from lib.leitura import *
import pyperclip

def enviar():
    pyautogui.PAUSE = 1

    # entrar no email
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
    pyautogui.press('Enter')
    sleep(2)

    pyautogui.click(x=79, y=173) # clica no botão de escrever email
    
    # preencher em email
    pyautogui.write('emailexemplo123321@gmail.com')
    pyautogui.press('tab') # tab para selecionar o email
    pyautogui.press('tab') # tab para mudar a área de digitação 

    pyperclip.copy('Relatório de Compras')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab') # tab para mudar a área de digitação

    pyperclip.copy(f"""
    Prezados,

    Segue o relatorio de compras
    Total Gasto: R${leitura()[0]:,.2f}
    Quantidade: {leitura()[1]:,}
    Preço Médio: R${leitura()[2]:,.2f}

    Qualquer dúvida é só falar.
    Att.,
    Usuário

    ps* no código não foi colocado a ação de enviar
    para evitar problemas
    """)

    pyautogui.hotkey('ctrl', 'v')
    # enviarMeu login
    # no código não foi colocado a ação de enviar para evitar problemas
