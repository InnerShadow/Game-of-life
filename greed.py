
import cell

import numpy as np

class Greed :

    def __init__(self, nrow, ncol, Matrix):
        self.ncol = ncol
        self.nrow = nrow
        self.Matrix = Matrix

        for i in range(ncol) :
            for j in range(nrow):
                Matrix[i][j] = cell.Cell(False)
                self.Matrix[i][j].doRandom()
        #}

    def CountNeighbours(self, i, j):
        neighbours = 0
        if i != self.ncol - 1 :
            if self.Matrix[i + 1][j].isAlive : neighbours += 1
        
        if i != self.ncol - 1 and j != self.nrow - 1 :
            if self.Matrix[i + 1][j + 1].isAlive : neighbours += 1
        
        if i != self.ncol - 1 and j != 0 :
            if self.Matrix[i + 1][j - 1].isAlive : neighbours += 1
        
        if j != self.nrow - 1:
            if self.Matrix[i][j + 1].isAlive : 
                neighbours += 1
        
        if j != 0 :
            if self.Matrix[i][j - 1].isAlive : neighbours += 1
        
        if i != 0 :
            if self.Matrix[i - 1][j].isAlive : neighbours += 1

        if i != 0 and j != self.nrow - 1 :
            if self.Matrix[i - 1][j + 1].isAlive : neighbours += 1

        if i != 0 and j != 0 :
            if self.Matrix[i - 1][j - 1].isAlive : neighbours += 1
        
        return neighbours


    def doLive(self) :
        tmp = np.ndarray(shape = (self.ncol, self.nrow), dtype = np.object_)
        tmp.fill(cell.Cell(False))
        for i in range(self.ncol) :
            for j in range(self.nrow) :
                val = self.Matrix[i, j]
                neighbours = self.CountNeighbours(i, j)
                if self.Matrix[i][j].isAlive :
                    if neighbours > 3 or neighbours < 2 :
                        tmp[i][j] = cell.Cell(False)
                if self.Matrix[i][j].isAlive and neighbours <= 3 and neighbours >= 2 :
                    tmp[i][j] = cell.Cell(True)
                if ~self.Matrix[i][j].isAlive and neighbours == 3 :
                    tmp[i][j] = cell.Cell(True)

        self.Matrix = tmp




