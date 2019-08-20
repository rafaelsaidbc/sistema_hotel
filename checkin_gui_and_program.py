import os
import pickle
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


class HOTEL_MANAGEMENT_checkin:
    def __init__(self):
        root = Tk()
        # configurações de fonte
        _bgcolor = 'ffffff'
        _fgcolor = '#000000'
        _compcolor = '#ffffff'
        _ana1color = '#ffffff'
        _ana2color = '#ffffff'

        font10 = '-family {Courier New} -size 10 -weight bold -slant ' \
                 'roman -underline 0 -overstrike 0'

        font11 = '-family {Segoe UI} -size 30 -weight bold -slant ' \
                 'roman -underline 0 -overstrike 0'

        font12 = '-family {Segoe UI} -size 18 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        font13 = '-family {Segoe UI} -size 17 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        font14 = '-family {Segoe UI} -size 16 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        font15 = '-family {Segoe UI} -size 19 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        font16 = '-family {Segoe UI} -size 15 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        font9 = '-family {Segoe UI} -size 9 -weight normal -slant ' \
                'roman -underline 0 -overstrike 0'

        # configurações da tela principal
        root.geometry('1069x690')
        root.title('Hotel Rafa Said')
        root.configure(background='cadetblue')
        root.configure(highlightbackground='#d9d9d9')
        root.configure(highlightcolor='black')
        root.wm_iconbitmap(r'icones/hotel.ico')

        # ========== TEXT BOX ==========
        self.Text1 = Text(root)
        self.Text1.place(relx=0.03, rely=0.65, relheight=0.29, relwidth=0.93)
        self.Text1.configure(background='white')
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground='black')
        self.Text1.configure(highlightbackground='#ffffff')
        self.Text1.configure(highlightcolor='black')
        self.Text1.configure(insertbackground='black')
        self.Text1.configure(selectbackground='#e6e6e6')
        self.Text1.configure(selectforeground='black')
        self.Text1.configure(width=880)
        self.Text1.configure(wrap=WORD)

        # ========== FRAMES ==========
        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth='10')
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background='#FF3E96')
        self.Frame1.configure(highlightbackground='#ffffff')
        self.Frame1.configure(highlightcolor='black')
        self.Frame1.configure(width=995)

        # ========== MESSAGES ==========
        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.5)
        self.Message1.configure(background='#FF3E96')
        self.Message1.configure(font=font11)
        self.Message1.configure(foreground='#000000')
        self.Message1.configure(highlightbackground='#ffffff')
        self.Message1.configure(highlightcolor='black')
        self.Message1.configure(text='Detalhes do cliente')
        self.Message1.configure(width=496)

        self.Message2 = Message(self.Frame1)
        self.Message2.place(relx=0.52, rely=0.19, relheight=0.74, relwidth=0.07)
        self.Message2.configure(background='#FF3E96')
        self.Message2.configure(font=font11)
        self.Message2.configure(foreground='#000000')
        self.Message2.configure(highlightbackground='#ffffff')
        self.Message2.configure(highlightcolor='black')
        self.Message2.configure(text=':')
        self.Message2.configure(width=66)

        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.57, rely=0.11, relheight=0.79, relwidth=0.35)
        self.Message3.configure(background='#FF3E96')
        self.Message3.configure(font=font11)
        self.Message3.configure(foreground='#000000')
        self.Message3.configure(highlightbackground='#ffffff')
        self.Message3.configure(highlightcolor='black')
        self.Message3.configure(text='Entrada')
        self.Message3.configure(width=347)

        root.mainloop()


if __name__ == '__main__':
    hotel = HOTEL_MANAGEMENT_checkin()
