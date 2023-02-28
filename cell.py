
from random import randint

class Cell :

    def __init__(self, isAlive = False) :
        sighn = randint(0, 10)
        if sighn != 0 :
            self.isAlive = False
        else :
            self.isAlive = True
        