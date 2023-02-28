
import cell as cell

import numpy as np

class Greed :

    def __init__(self, nrow, ncol, Matrix) :
        self.ncol = ncol
        self.nrow = nrow
        self.Matrix = Matrix

        for i in range(ncol) :
            for j in range(nrow) :
                Matrix[i][j] = cell.Cell()
        #}

