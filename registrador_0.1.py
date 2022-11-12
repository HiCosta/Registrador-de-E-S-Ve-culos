from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime as dt

def registrador():
    layout_menu = [['Arquivo', ['Gerar Relatório', 'Encaminha para E-mail']],
                   ['Opções', ['Alterar Tema', 'Voltar a Tela de Login']],
                   ['Ajuda', ['Manual do Software', 'Contato Desenvolvedor',['E-mail: samuel0100wanderson@gmail.com', 'higor_scosta@outlook.com']]]]

    hh_entrada = int(dt.today().strftime('%H'))
    mm_entrada = int(dt.today().strftime('%M'))
    hh_saida = int()
    mm_saida = int()
    valor_servico = float()
    
    if hh_entrada >= hh_saida:          #calculando tempo de estadia do veiculo no estacionamento
        hh_estadia = hh_entrada - hh_saida
    else:
        hh_estadia = hh_saida - hh_entrada
        
    if mm_entrada >= mm_saida:
        mm_estadia = mm_entrada - mm_saida
    else:
        mm_estadia = mm_saida - mm_entrada
 
   
    padrao = 'DarkPurple7'
    cor2 = 'SystemDefaultForReal'
    cor3 = 'Black'
    tema = sg.theme(padrao)
    tema
    linha = [
        [sg.Menu(layout_menu, background_color="white", text_color="black", key='aba')],
        [sg.Text('Placa'), sg.Text('          Modelo/cor'), sg.Text('               Entrada'), sg.Text('    Saída'), sg.Text('  Valor do Serviço')],
        [sg.Input('',size=(9, 1)), sg.Input('',size=(20, 1)), sg.Input(hh_entrada, size=(2, 1)), sg.Input(mm_entrada, size=(2, 1)), sg.VerticalSeparator(), sg.Input(hh_saida, size=(2, 1), key= 'update1'), sg.Input(mm_saida, size=(2, 1), key= 'update2'),  sg.Button('※', button_color=("Grey")), sg.Input(valor_servico, size=(14, 1), key= 'update3')],
    ]
    
    
    layout2 = [
        [sg.Frame('Registrador', layout=linha, key='container')],
        [sg.Button('Adicionar Registro'), sg.Button('Resetar Registros')]
    ]

    return sg.Window('Registro de Veículos', layout=layout2, resizable=True, finalize=True)


janela2 = registrador()
# Regras da Janela
while True:
    eventos2, valores2 = janela2.read(timeout=1)

    if eventos2 == sg.WINDOW_CLOSED: #Permitindo que seja encerrado programa
        break
    elif eventos2 == 'Adicionar Registro':
        hh_entrada = int(dt.today().strftime('%H'))
        mm_entrada = int(dt.today().strftime('%M'))
        hh_saida = int()
        mm_saida = int()
        hh_estadia, mm_estadia = int()
        valor_servico = float()
                    
        eventos2 = janela2.extend_layout(janela2['container'], [[sg.Input('',size=(9, 1)), sg.Input('',size=(20, 1)), sg.Input(hh_entrada, size=(2, 1)), sg.Input(mm_entrada, size=(2, 1)), sg.VerticalSeparator(), sg.Input(hh_saida, size=(2, 1), key= 'update2'), sg.Input(mm_saida, size=(2, 1), key= 'update1'),  sg.Button('※', button_color=("Grey")), sg.Input(valor_servico, size=(14, 1), key= 'update3')]]),

    elif eventos2 == 'Resetar Registros':
        sg.theme('DarkPurple5')
        sim = 'Sim'
        nao = 'Não'
        answer = sg.popup('Se confirmar isso irá apagar todos os registros!\nTem certeza?', font='Arial', custom_text=(sim, nao), background_color= 'Brown', title='Aviso')
        sg.theme('DarkPurple7')
        if answer == nao:
            ()
        elif answer == sim:
            janela2.close()
            janela2 = registrador()
        else: ()
    elif eventos2 == '※':
        
        hh_entrada = int(dt.today().strftime('%H'))
        mm_entrada = int(dt.today().strftime('%M'))
        hh_saida = int()
        mm_saida = int()
        hh_estadia, mm_estadia = float()
        valor_servico = int()   
                
        if hh_estadia == 1 and mm_estadia == 0:     #calclulando valor do servico de acordo com estadia
            valor_servico = 7
        elif hh_estadia == 0 and mm_estadia > 0:
            valor_servico = mm_estadia * 0.05
        elif hh_estadia > 1 and mm_estadia == 0:
            valor_servico = hh_estadia * 7
        elif hh_estadia > 1 and mm_estadia > 0:
            valor_servico = (hh_estadia * 7) + (mm_estadia * 0.05)
        
        janela2['update1'].update(int(dt.today().strftime('%H')))
        janela2['update2'].update(int(dt.today().strftime('%M')))
        janela2['update3'].update(valor_servico)
