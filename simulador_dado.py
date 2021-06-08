#Simulador de dado
#Simular o uso de um dado, gerando um valor de 1 a 6
import random
import PySimpleGUI as sg

class SimuladorDados:
    
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #Criar layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('SIM'),sg.Button('NAO')],
            [sg.Button('Encerrar')]
        ]
        
    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de dado',layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores
        try:
            if self.eventos == 'SIM' or self.eventos == 's':
                self.GerarValorDado()
            elif self.eventos == 'NAO' or self.eventos == 'n':
                print('Agradecemos sua participação.\n')
            elif self.eventos == 'Encerrar':
                    print('Encerrando o Jogo')
            else:
                print('Favor digitar SIM ou NAO')
        except:
            print('Ocorreu um erro ao receber sua resposta')
                
    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
  

simulador = SimuladorDados()
simulador.Iniciar()