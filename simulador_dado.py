#Simulador de dado
#Simular o uso de um dado, gerando um valor de 1 a 6
import random

class SimuladorDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDado()
            elif resposta == 'nao' or resposta == 'n':
                print('Agradecemos sua participação')
            else:
                print('Favor digitar sim ou nao')
        except:
            print('Ocorreu um erro ao receber sua resposta')
            
            
    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        

simulador = SimuladorDado()
simulador.Iniciar()