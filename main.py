import tkinter as tk
import time
from selenium import webdriver
import pyautogui as pg
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
from tkinter import messagebox
import os
from tkinter import font


def coletas_cwb():
    # Abra a página da web
        time.sleep(1.0)
        driver = webdriver.Chrome()
        # Abra a página da web
        driver.get('https://sistema.ssw.inf.br/bin/ssw0422')
        pg.sleep(0.5)
        pg.hotkey('win', 'up')
        pg.moveTo(x=650, y=194)
        pg.click()

        # login
        pg.write('rvi')
        pg.write('13524737986')
        pg.write('mateusf')
        pg.press('tab')
        pg.write('mateus21')
        pg.press('enter')
        pg.sleep(2.0)

        # Selecionar
        pg.click(x=189, y=195)
        pg.write('103')
        pg.sleep(0.8)
        pg.click(x=345, y=352)
        pg.sleep(1.2)
        pg.scroll(-300)
        pg.sleep(1.0)

        # achar elemento
        element_location = pg.locateOnScreen('C:/Users/User/Desktop/Docs/Programas/Coletas/elementox.png', confidence=0.8)
        if element_location:
            # Obtenha as coordenadas do centro do elemento
            x_pos, y_pos = pg.center(element_location)
            # Mova o mouse para as coordenadas do elemento
            pg.moveTo(x_pos, y_pos)

        # copiar dados tabela
        pg.move(30, 0)
        pg.hotkey('ctrl', 'a')
        pg.keyDown('shift')
        pg.click()
        pg.keyUp('shift')
        pg.hotkey('ctrl', 'c')

        # abrir coletas e colar tabela
        pg.moveTo(x=75, y=745)
        pg.rightClick()
        pg.sleep(0.8)
        element_location = pg.locateOnScreen('C:/Users/User/Desktop/Docs/Programas/Coletas/chcol.png',confidence=0.8)
        if element_location:
            x_pos, y_pos = pg.center(element_location)
            pg.moveTo(x_pos, y_pos)
        pg.click()
        pg.sleep(10)

        pg.click(x=230, y=714)
        pg.click(x=57, y=282)
        pg.sleep(0.5)

        pg.hotkey('ctrl', 'v')
        pg.sleep(1.3)
        pg.sleep(0.8)

       # Abrir limpo e copiar
        pg.click(x=369, y=700)
        pg.sleep(1.3)

        pg.click(x=301, y=262)
        time.sleep(1.0)
        pg.hotkey('ctrl', 'c')

        # Colar Whatsapp
        pg.click(x=115, y=19)
        pg.sleep(2)
        pg.click(x=115, y=335)
        pg.sleep(0.8)
        pg.press('enter')
        pg.sleep(0.5)
        pg.hotkey('ctrl', 'v')
        pg.sleep(0.5)
        pg.press('enter')
        pg.sleep(2)

        # fechar
        element_location = pg.locateOnScreen('C:/Users/User/Desktop/Docs/Programas/Coletas/elecoleta.png',confidence=0.8)
        if element_location:
            x_pos, y_pos = pg.center(element_location)
            pg.moveTo(x_pos, y_pos)
        pg.click()
        pg.hotkey('ctrl', 'w')

def coletas_bnu():
    # Abra a página da web
        time.sleep(1.0)
        driver = webdriver.Chrome()
        # Abra a página da web
        driver.get('https://sistema.ssw.inf.br/bin/ssw0422')
        pg.sleep(0.5)
        pg.hotkey('win', 'up')
        pg.moveTo(x=650, y=194)
        pg.click()

        # login
        pg.write('rvi')
        pg.write('13524737986')
        pg.write('mateusf')
        pg.press('tab')
        pg.write('mateus21')
        pg.press('enter')
        pg.sleep(2.0)

        # Selecionar
        pg.hotkey('shift', 'tab')
        pg.write('BNU')
        pg.click(x=189, y=195)
        pg.write('103')
        pg.sleep(0.8)
        pg.click(x=345, y=352)
        pg.sleep(1.2)
        pg.scroll(-300)
        pg.sleep(1.0)

        # achar elemento
        element_location = pg.locateOnScreen('C:/Users/User/Desktop/Docs/Programas/Coletas/elementox.png', confidence=0.8)
        if element_location:
            # Obtenha as coordenadas do centro do elemento
            x_pos, y_pos = pg.center(element_location)
            # Mova o mouse para as coordenadas do elemento
            pg.moveTo(x_pos, y_pos)

        # copiar dados tabela
        pg.move(30, 0)
        pg.hotkey('ctrl', 'a')
        pg.keyDown('shift')
        pg.click()
        pg.keyUp('shift')
        pg.hotkey('ctrl', 'c')

        # abrir coletas e colar tabela
        pg.moveTo(x=75, y=745)
        pg.rightClick()
        pg.sleep(0.8)
        element_location = pg.locateOnScreen('C:/Users/User/Desktop/Docs/Programas/Coletas/chcol.png',confidence=0.8)
        if element_location:
            x_pos, y_pos = pg.center(element_location)
            pg.moveTo(x_pos, y_pos)
        pg.click()
        pg.sleep(10)

        pg.click(x=496, y=709)
        pg.click(x=57, y=282)
        pg.sleep(0.5)

        pg.hotkey('ctrl', 'v')
        pg.sleep(1.3)
        pg.sleep(0.8)

       # Abrir limpo e copiar
        pg.click(x=613, y=700)
        pg.sleep(1.3)

        pg.click(x=301, y=262)
        time.sleep(1.0)
        pg.hotkey('ctrl', 'c')

        # Colar Whatsapp
        pg.click(x=115, y=19)
        pg.sleep(2)
        pg.click(x=115, y=335)
        pg.sleep(0.8)
        pg.press('enter')
        pg.sleep(0.5)
        pg.hotkey('ctrl', 'v')
        pg.sleep(0.5)
        pg.press('enter')
        pg.sleep(2)

        # fechar
        element_location = pg.locateOnScreen('C:/Users/User/Desktop/Docs/Programas/Coletas/elecoleta.png',confidence=0.8)
        if element_location:
            x_pos, y_pos = pg.center(element_location)
            pg.moveTo(x_pos, y_pos)
        pg.click()
        pg.hotkey('ctrl', 'w')

def checklist():
    #Abrir planilha
    pg.moveTo(x=75, y=745)
    pg.rightClick()
    pg.sleep(0.6)
    element_location = pg.locateOnScreen('C:/Users/User/Desktop/Docs/Programas/Coletas/chcol.png', confidence=0.8)
    if element_location:
        x_pos, y_pos = pg.center(element_location)
        pg.moveTo(x_pos, y_pos)
    pg.click()    
    pg.sleep(5.0)
    pg.moveTo(x=731, y=712)
    pg.click()

    #copiar e colar whatsapp

    #JOI
    pg.click(122, 257)
    pg.sleep(0.7)
    pg.hotkey('ctrl','c')
    #WhatsJOI
    pg.click(115, 19)
    pg.sleep(0.7)
    pg.click(291, 198)
    pg.write('JOI - Unidade Parceiro')
    pg.sleep(0.7)
    pg.click(281, 339)
    pg.sleep(0.5)
    pg.press('enter')
    pg.hotkey('ctrl', 'v')
    pg.sleep(0.6)
    pg.press('enter')
    pg.sleep(0.8)

    #BNU
    element_location = pg.locateOnScreen('C:/Users/User/Desktop/Docs/Programas/Coletas/elecoleta.png', confidence=0.8)
    if element_location:
        # Obtenha as coordenadas do centro do elemento
        x_pos, y_pos = pg.center(element_location)
        # Mova o mouse para as coordenadas do elemento
        pg.moveTo(x_pos, y_pos)
    pg.click()

    pg.click(289, 259)
    pg.sleep(0.7)
    pg.hotkey('ctrl','c')
    #WhatsBNU
    pg.click(115, 19)
    pg.sleep(0.7)
    pg.click(291, 198)
    pg.write('BNU - Unidade Parceiro')
    pg.sleep(0.7)
    pg.click(281, 339)
    pg.sleep(0.5)
    pg.press('enter')
    pg.hotkey('ctrl', 'v')
    pg.sleep(0.6)
    pg.press('enter')
    pg.sleep(0.8)

    #SJB
    element_location = pg.locateOnScreen('C:/Users/User/Desktop/Docs/Programas/Coletas/elecoleta.png', confidence=0.8)
    if element_location:
        # Obtenha as coordenadas do centro do elemento
        x_pos, y_pos = pg.center(element_location)
        # Mova o mouse para as coordenadas do elemento
        pg.moveTo(x_pos, y_pos)
    pg.click()

    pg.click(453, 261)
    pg.sleep(0.5)
    pg.hotkey('ctrl','c')
    #WhatsSJB
    pg.click(115, 19)
    pg.sleep(0.7)
    pg.click(291, 198)
    pg.write('SJB - Unidade Parceiro')
    pg.sleep(0.7)
    pg.click(281, 339)
    pg.sleep(0.5)
    pg.press('enter')
    pg.hotkey('ctrl', 'v')
    pg.sleep(0.6)
    pg.press('enter')
    pg.sleep(0.8)

def CheckColetas():
    # Obtém o diretório do script1.py
    diretorio_script1 = os.path.dirname(os.path.abspath(__file__))

    # Constrói o caminho completo para script2.py no diretório /outro_diretorio
    caminho_script2 = os.path.join(diretorio_script1, '..', 'C:/Users/User/Desktop/Docs/Programas/CheckColetas', 'main.py')

    # Comando para executar script2.py em um novo processo
    os.system(f'python {caminho_script2}')         

def Coletas():
     coletas_cwb()
     coletas_bnu()

janela = tk.Tk()

# Definir dimensões da janela (largura x altura + posição_x + posição_y)
largura = 230
altura = 200
posicao_x = 20
posicao_y = 20
janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")
janela.title("Central Coletas")
janela.iconbitmap('C:/Users/User/Desktop/Docs/Programas/Coletas/box.ico')
janela.resizable(False, False)
my_font = font.Font(family="Aptos Mono", size=9)
janela.configure(bg='lightgray')

# Botão para executar o Script 1
botao_script1 = tk.Button(janela, text="Post (CWB)", command=coletas_cwb, font=my_font, padx=70)
botao_script1.grid(pady=10, padx=10, column=1, row=1)

# Botão para executar o Script 2
botao_script2 = tk.Button(janela, text="Post (BNU)", command=coletas_bnu, font=my_font, padx=70)
botao_script2.grid(pady=10, padx=10, column=1, row=2)

# Botão para executar o Script 3

botao_script3 = tk.Button(janela, text="Post (CWB / BNU)", command=Coletas, font=my_font, padx=50)
botao_script3.grid(pady=10, padx=10, column=1, row=3)

# Botão para executar o Script 4
botao_script4 = tk.Button(janela, text="Checklist (BNU)", command=checklist, font=my_font, padx=55)
botao_script4.grid(pady=10, padx=10, column=1, row=4)

# Botão para executar o Script 5
#botao_script5 = tk.Button(janela, text="Coletas (Baixar) ", command=CheckColetas)
#botao_script5.pack(pady=10)

# Rodar o loop principal
janela.mainloop()
