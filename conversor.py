# Conversor de Unidades (mL -> L, L -> mL, ...) <>

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

# Interface do Programa <>

unidades = ['mL','L','cm³']
areas = ['Volume']

colunaConverter = [
    [sg.Input(default_text='Digite o valor desejado aqui', size=(40,1), key='NConverter'), sg.Combo(values=unidades, default_value='mL', key='CConverter')],
    [sg.Listbox(values=areas, default_values='Volume', size=(38,6))],
    [sg.Button('Converter')]
]

colunaConvertido = [
    [sg.Text(size=(35,1), background_color='white', text_color='black', key='NConvertido'), sg.Combo(values=unidades, default_value='L', key='CConvertido')],
    [sg.Listbox(values=areas, default_values='Volume', size=(38,6), key='LArea')],
    [sg.Button('Limpar')]
]

layout = [
    [sg.Column(colunaConverter), sg.VSeparator(), sg.Column(colunaConvertido)]
]

window = sg.Window('Conversor de Unidades', layout)

while True:

    event, values = window.read()

    if event == WINDOW_CLOSED:
        break

    elif event == 'Converter':

        try:

                txtCI = float(values['NConverter'])

        except:

            sg.Popup('Erro', 'Digite um número legível.') 
        
        else:
        
            if values['CConverter'] == 'mL' and values['CConvertido'] == 'L' or values['CConverter'] == 'cm³' and values['CConvertido'] == 'L':
            
                txtCII = txtCI / 1000

                window['NConvertido'].update(txtCII)

            elif values['CConverter'] == 'L' and values['CConvertido'] == 'mL' or values['CConverter'] == 'L' and values['CConvertido'] == 'cm³':

                txtCII = txtCI * 1000

                window['NConvertido'].update(txtCII)

            elif values['CConverter'] == 'cm³' and values['CConvertido'] == 'mL' or values['CConverter'] == 'mL' and values['CConvertido'] == 'cm³' or values['CConverter'] == values['CConvertido']:

                window['NConvertido'].update(txtCI)

    elif event == 'Limpar':

        window['NConverter'].update('')
        window['NConvertido'].update('')


