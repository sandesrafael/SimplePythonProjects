# Projeto 3 - Chute o número
# Objetivo:  Criar um algoritmo que gera um valor aleatório, onde o usuário precisa tentar acertar qual é esse valor

import random
import PySimpleGUI as sg
import time 

#Class
class GuessANumber:
    
    #Initial function to set default values
    def __init__(self):
        self.min_value = 1
        self.max_value = 100
        self.random_value = 0
        self.try_again = True

    #Responsible function for starting the program
    def Start(self):
        
        #Create a layout for the graphical interface
        layout = [
            [sg.Text('Enter your guess: ',size=(39,0))],
            [sg.Input(size=(18,0),key='ChosenValue')],
            [sg.Button('Guess')],
            [sg.Output(size=(39,10))],
            [sg.Button('Close')]
        ]
        
        #Create a window for the graphical interface
        self.window = sg.Window('Enter a guess!',layout=layout)
        self.CreateRandomNumber()
        try:
            while True:
                # Receive the values
                self.events, self.values = self.window.Read()
                
                # Do something with these values
                if self.events == 'Guess':
                    self.answer = self.values['ChosenValue']
                    while self.try_again == True:
                        if int(self.answer) > self.random_value:
                            print('You missed! Enter a lower value!')
                            break
                        elif int(self.answer) < self.random_value:
                            print('You missed! Enter a higher value')
                            break
                        if int(self.answer) == self.random_value:
                            self.try_again = False
                            print('Congratulations. You Win!!')
                            break
                elif self.events in ('Close', sg.WINDOW_CLOSED):
                    print('Closing...')
                    time.sleep(1.2)
                    break
        except:
            print('Please, type a integer number')
            self.Start()
    
        #Close the Window
        self.window.close()
        
    #Function to create a random number using randint
    def CreateRandomNumber(self):
        self.random_value =  random.randint(self.min_value, self.max_value)

guess = GuessANumber()
guess.Start() 