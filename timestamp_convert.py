from tkinter import Event
import PySimpleGUI as sg 
from datetime import datetime
from pytz import timezone
import pytz

# print(pytz.all_timezones) ## Todas as timezones disponiveis

def convert_timestamp(value): 

    try:        
        timestamp = float(value)        
        dt = datetime.fromtimestamp(timestamp, tz = timezone("America/Sao_Paulo"))       
        dt = (dt.strftime ("%d/%m/%Y %H:%M:%S")) #("%d/%m/%Y %H:%M:%S.%f %z")) # 08/10/2015 06:30:22.348341 +0900
        return dt  

    except ValueError:
        print("não foi possível converter o valor do timestamp para um número")

def janela1():
    sg.theme('Reddit')
    layout = [
        [sg.Text('De Timestamp para Data')],
        [sg.Input(key='timestamp')],
        [sg.Submit(), sg.Cancel()] 
    ]
    return sg.Window('Convert Timestamp', layout=layout, finalize=True )

janela1 = janela1()

while True:
    window, event, values = sg.read_all_windows()
    
    if window == janela1 and event == sg.WIN_CLOSED or window == janela1 and event == "Cancel":
        break

    if window == janela1 and event == "Submit": 
        timestamp = values['timestamp'] 
        if timestamp.isdigit() and len(timestamp) > 0:
            data = convert_timestamp(values['timestamp']) 

            resposta = data                             
           
            sg.popup('Data', resposta)
        else:
            sg.popup('Insira dados validos')
    
  
