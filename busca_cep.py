from tkinter import Event
import PySimpleGUI as sg 
import requests
import json

def buscar_dados_id(cep):
    r = requests.get(f"http://viacep.com.br/ws/{cep}/json/")     
    if r.status_code == 200:
        dados = json.loads(r.content)        
        if 'erro' in dados and dados['erro'] == True:
            dados = 'Nao ha dados para este CEP'        
    else:
        dados = r.status_code   
    return dados

def busca_cep():
    sg.theme('Reddit')
    layout = [
        [sg.Text('CEP')],
        [sg.Input(key='cep')],
        [sg.Submit(), sg.Cancel()] 
    ]
    return sg.Window('Busca de CEP', layout=layout, finalize=True )

janela1 = busca_cep()

while True:
    window, event, values = sg.read_all_windows()
    
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == "Submit": 
        cep = values['cep'] 
        if cep.isdigit() and len(cep) == 8:
            dados_cep = buscar_dados_id(values['cep']) 

            resposta = dados_cep                             
           
            sg.popup('Dados do CEP', resposta)
        else:
            sg.popup('Insira dados de CEP validos')
    
  
