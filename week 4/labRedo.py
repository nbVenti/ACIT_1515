import random

class numberGame:
    def __init__(self,num_guesses):
        self.num_guesses = num_guesses
        self.u = self.convert(self.num_guesses)    
        self.i = self.getRandomNumber()
        self.guesed_correctly = False
        self.counter = 0
        self.question()
    
    def linkStart(self):
        start = numberGame(input("Input Max guesses\n\n"))
    
    def prompt(self,message):
        x = input(message)
        return x

    def getRandomNumber(self):
        i = random.randrange(self.u)
        return i


    def question(self):
        x = self.prompt("enter Guess\n")
        x = self.convert(x)
        if self.counter > self.u:
            self.again( False)
        if x != self.i:
            self.counter += 1
            self.question()
        else:
            self.guesed_correctly = True
            self.again(self.guesed_correctly)

    def again(self,x):
        if x:
            print("You got it right")
        y = self.prompt("Play again")
        if y == "n":
            exit()
        else:
            self.linkStart(self)
    
    def convert(self,x):
        u = int(x)
        return (u)

numberGame.linkStart(None)