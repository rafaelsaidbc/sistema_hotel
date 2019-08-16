import os
#importa outros arquivos
from subprocess import call
from tkinter import messagebox
import sys
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk


# cria a classe principal
class HOTEL_MANAGEMENT:
    def __init__(self):
        # inicia o root
        root = Tk()


        # executa o root
        root.mainloop()

# se a classe HOTEL_MANAGEMENT existir, chama o __main__
if __name__ == '__main__':
    GUEST = HOTEL_MANAGEMENT()