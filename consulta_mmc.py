from tkinter import Event
import PySimpleGUI as sg 
import csv

import os
path = os.getcwd()

def mmc_codes(mmc_number:str = None, description:str = None):
    
    with open('mcc_codes.csv', encoding='utf-8') as arquivo_referencia:
        tabela = csv.reader(arquivo_referencia, delimiter=',')         
        # Se encontrar o mmc na lista retorna mmc e descrição
        if mmc_number is not None and len(mmc_number) == 4 :
            for l in tabela:
                if mmc_number == l[0]:
                    return {l[0], l[1]}
        # Se contiver a description informada em parte da descrição retorna mmc e descrição
        if description is not None:
            possiveis = {}
            for l in tabela:
                if description in l[1]:
                    possiveis[l[0]] = l[1]
            return possiveis        
        return ("Nenhum item encontrado para os campos", mmc_number, description)

# Constroi a janela
def mmc_dados():
    sg.theme('Reddit')
    layout = [
        [sg.Text('MMC')],
        [sg.Input(key='mmc')],
        [sg.Submit(), sg.Cancel()] 
    ]
    return sg.Window('Busca MMC', layout=layout, finalize=True )

janela1 = mmc_dados()

while True:
    window, event, values = sg.read_all_windows()
    
    if window == janela1 and event == sg.WIN_CLOSED or window == janela1 and event == "Cancel":
        break

    if window == janela1 and event == "Submit": 
        mmc = values['mmc'] 
        if mmc.isdigit() and len(mmc) == 4:
            dados_mmc = mmc_codes(values['mmc']) 
            resposta = dados_mmc
            sg.popup('Dados do MMC', resposta)
        elif len(mmc) > 3:
            dados_mmc = mmc_codes(None, values['mmc'])
            resposta = dados_mmc
            sg.popup('Dados do MMC', resposta) 
        else:
            sg.popup('Dados aceitos 4 numeros interios ou Palavras em ingles que possam conter na description do MMC')
    
  
