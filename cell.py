
from random import randint

class Cell :

    def doRandom(self) :
        sighn = randint(0, 8)
        if sighn != 0 :
            self.isAlive = False
        else :
            self.isAlive = True
        
    def __init__(self, isAlive) :
        self.isAlive = isAlive