# Project 7 - Adventure Game
# A decision game where I'll have to create several different endings, based on the answers given

# I wanna reach different endings in my story, based on the answers that I give to the program


#I'm in a war between two nations, and we have two sides: Side A and Side B. 
# Only side A will win, and Side B will lose. 
# So I have to make the right decisions to get to victory, which only Side A will do. 
import PySimpleGUI as sg
import time
class AdvantureGame():
    def __init__(self):
        self.question1 = 'Were you born in the North or South? (n/s)' # North = SideA, South = SideB
        self.question2 = 'Do you prefer the sword or the shield? (sword/shield)' # Sword = SideA, Shield = SideB
        self.question3 = 'What is your specialty? (front lines / tatical)' # front line = SideA, Tatical = SideB
        self.storyEnd1 = 'You will be a hero on the front lines!'
        self.storyEnd2 = 'You will be a hero protecting all our troops !'
        self.storyEnd3 = 'You will sacrifice yourself in battle!'
        self.storyEnd4 = 'You are not able to fight this battle!'
        
    def Start(self):
        #Layout
        layout = [
            [sg.Output(size=(50,0))],
            [sg.Input(size=(25,0),key='choose')],
            [sg.Button('Iniciar'),sg.Button('Answer'), sg.Button('Exit')]
        ]
        #Window
        self.window = sg.Window('Advanture Game', layout=layout)
        while True:
            #Read a values
            self.readValues()
            #Do something with the values
            if self.events == 'Iniciar':
                print(self.question1)
                self.readValues()
                if self.values['choose'] == 'n':
                    print(self.question2)
                    self.readValues()
                    if self.values['choose'] == 'sword':
                        print(self.storyEnd1)
                    if self.values['choose'] == 'shield':
                        print(self.storyEnd2)
                if self.values['choose'] == 's':
                    print(self.question3)
                    self.readValues()
                    if self.values['choose'] == 'front lines':
                            print(self.storyEnd3)
                    if self.values['choose'] == 'tatical':
                        print(self.storyEnd4)
            elif self.events in ('Exit', sg.WINDOW_CLOSED):
                print('\n\nClosing...')
                time.sleep(0.8)
                break
                
                
    def readValues(self):
        self.events, self.values = self.window.Read()
            
game = AdvantureGame()
game.Start()