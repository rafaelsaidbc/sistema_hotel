from __main__ import *
import sys
# importa outros arquivos
from subprocess import call
from tkinter import messagebox

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

# caebeçalho armazenado na variável p
p = '''
    ========== HOTEL RAFA SAID | 5 ESTRELAS ==========
    ================= ENDEREÇO ================
    =============  SERVINDO DESDE 2019 ============
    =============== ### DATA ### ===============
    ========================================
    
    
    NOME: %S
    ENDEREÇO: %S
    TELEFONE: %S
    TOTAL DA CONTA: R$%S
    QUARTO: %S'''


# classe principal do recibo
class recipt:
    def __init__(self):
        root = Tk()
        # configurações de fonte
        _bgcolor = 'ffffff'
        _fgcolor = '#000000'
        _compcolor = '#ffffff'
        _ana1color = '#ffffff'
        _ana2color = '#ffffff'

        # font11 -size 17
        font16 = '-family {Segoe UI} -size 16 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        # font14 -size 16
        font17 = '-family {Segoe UI} -size 17 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        # configurações da tela principal
        root.geometry('800x600')
        root.title('Hotel Rafa Said | Recibo')
        root.configure(background='#d9d9d9')
        root.wm_iconbitmap(r'icones/hotel.ico')

        # ========== LABELS ==========
        # Label1 fica dentro do root
        self.Label1 = Label(root)
        self.Label1.place(relx=0, rely=0, height=800, width=800)
        self.Label1.configure(background='#d9d9d9')
        self.Label1.configure(disabledforeground='#a3a3a3')
        self.Label1.configure(anchor=N)
        self.Label1.configure(foreground='#000000')
        self.Label1.configure(text=p)
        self.Label1.configure(wraplength=1000)
        self.Label1.configure(justify=LEFT)
        self.Label1.configure(width=582)

        root.mainloop()

if __name__ == '__main__':
    recipt1 = recipt()
