# Projeto 3 - Chute o número
# Objetivo:  Criar um algoritmo que gera um valor aleatório, onde o usuário precisa tentar acertar qual é esse valor

import random

class GuessANumber:
    def __init__(self):
        self.min_value = 1
        self.max_value = 100
        self.random_value = 0
        self.try_again = True

    def Start(self):
        self.CreateRandomNumber()
        self.AskRandomNumber()
        
        try:
            while self.try_again == True:
                if int(self.answer) > self.random_value:
                    print('You missed! Enter a lower value')
                    self.AskRandomNumber()
                elif int(self.answer) < self.random_value:
                    print('You missed! Enter a higher value')
                    self.AskRandomNumber()
                else:
                    self.try_again = False
                    print('Congratulations. You Win!!')
        except:
            print('Please, type a integer number')
            self.Start()
      
                
    def AskRandomNumber(self):
        self.answer = input('Enter your guess: ')

    def CreateRandomNumber(self):
        self.random_value = random.randint(self.min_value, self.max_value)


guess = GuessANumber()
guess.Start()