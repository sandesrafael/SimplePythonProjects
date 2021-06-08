#Simulador de dado
#Simular o uso de um dado, gerando um valor de 1 a 6
import random

class SimuladorDados:
    
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
    
    def Iniciar(self):
        
        resposta = input(self.mensagem)
        try:
            if resposta == 's' or resposta == 'sim':
                self.GeraValorDado()
            elif resposta == 'n' or resposta == 'nao':
                print('Encerrando o programa...')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')
                
    def GeraValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
    
    
simulador = SimuladorDados()
simulador.Iniciar()