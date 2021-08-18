from calendar import c
import PySimpleGUI as sg

class Telapython:
    def __init__(self):
        #layout

        layout = [
            [sg.Text('NOME',size=(5,0)),sg.Input(size=(20,0),key='nome')],
            [sg.Text('idade',size=(5,0)),sg.Input(size=(20,0),key='idade')],
            [sg.Text('CPF',size=(5,0)),sg.Input(size=(20,0),key='cpf')],
            [sg.Text('Email',size=(5,0)),sg.Input(size=(20,0),key='email')],
            [sg.Text('Tipo de Email',size=(15,0))],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Button('Enviar')],
            {sg.Output(size=(30,15))}


        ]
        # Janela

        self.janela = sg.Window("Dados do usuario").layout(layout)

        # Retirar dados na tela
        self.Button, self.values = self.janela.read()

    def Iniciar(self):
        while(1):
            self.Button, self.values = self.janela.read()
            nome = self.values['nome'] 
            idade = self.values['idade'] 
            cpf = self.values['cpf'] 
            email = self.values['email'] 
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook'] 
            aceita_yahoo = self.values['yahoo'] 
            print(f'nome:{nome}')  
            print(f'idade:{idade}') 
            print(f'CPF:{cpf}') 
            print(f'Email:{email}')
            print(f'aceita_gmail:{aceita_gmail}') 
            print(f'aceita_outlook:{aceita_outlook}')
            print(f'aceita_yahoo:{aceita_yahoo}') 
        

tela = Telapython()
tela.Iniciar()