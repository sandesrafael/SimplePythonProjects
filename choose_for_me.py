# Project 5 - Choose for me
# Ask the program a question and it will have to give you an answer.

# Project 6 - Graphical Interface (Project 5)
import random
import time
import PySimpleGUI as sg
import fileinput as fileobj


class ChooseForMe:
    def __init__(self):
        self.boolean = True
    
    def Start(self):
        # Creat a layout to the program
        self.layout = [
            [sg.Text('Ask your question: ')],
            [sg.Input(size=(40,0))],
            [sg.Button('Choose for me')],
            [sg.Output(size=(40,10))],
            [sg.Button('Exit')]
        ]
        #Create a window
        self.window = sg.Window("Choose for me", layout=self.layout)
        while True:
            self.events, self.values = self.window.Read()
            
            if self.events == 'Choose for me':            
                while self.boolean == True:
                    self.RandomAnswers()
                    break
            
            elif self.events in ('Exit', sg.WINDOW_CLOSED):
                print('\n\nClosing...')
                time.sleep(0.8)
                break
            

    def RandomAnswers(self):
        
        self.fileobj = open('/Git/repositorio/ProjetosPython/ProjetosPython/answers.csv','r')
        self.lines = []
        
        for self.line in self.fileobj:
            self.lines.append(self.line.strip())
        
        print(random.choice(self.lines))
            
        
       
        

choice = ChooseForMe()
choice.Start()