
from PyQt5.QtWidgets import *
import sys

import numpy as np
import greed
import Window


def __main__() :

    ncol = 90
    nrow = 60
    
    _greed = greed.Greed(nrow, ncol, np.ndarray(shape = (ncol, nrow), dtype = np.object_))

    App = QApplication(sys.argv)
    window = Window.Window(_greed)
    sys.exit(App.exec())

if __name__ == '__main__' :
    __main__()

