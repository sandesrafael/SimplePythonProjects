# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 a 6
import random
import PySimpleGUI as sg


class SimuladorDados:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        
        # Criar layout
        self.layout = [
            [sg.Text("Deseja jogar o dado?")],
            [sg.Button("SIM"), sg.Button("NAO")],
            [sg.Button("ENCERRAR")]
        ]

    def Iniciar(self):
        # Criar uma janela
        self.window = sg.Window("Simulador de dado",layout=self.layout)
        # Ler os valores da tela
        self.events, self.values = self.window.Read()
        # Fazer alguma coisa com esses valores
        
        try:
            if self.events == 's' or self.events == 'SIM':
                self.GerarValorDado()
            elif self.events == 'n' or self.events == 'NAO':
                print('Agradecemos por sua participação!')
            elif self.events == 'ENCERRAR':
                print('print("Encerrando o programa.")')
            else:
                print('Favor digitar sim/nao ou encerrar')
        except:
            print('Ocorreu um erro ao receber sua resposta')
        

    def GerarValorDado(self):
        print(random.randint(self.min_value, self.max_value))

simulador = SimuladorDados()
simulador.Iniciar()