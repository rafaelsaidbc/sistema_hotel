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

        # font11 -size 17
        font16 = '-family {Segoe UI} -size 16 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        # font14 -size 16
        font17 = '-family {Segoe UI} -size 17 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        # configurações da tela principal
        root.geometry('780x541+504+123')
        root.title('Hotel Rafa Said')
        root.configure(background='#ffffff')
        root.configure(highlightbackground='#ffffff')
        root.configure(highlightcolor='black')
        root.wm_iconbitmap(r'icones/hotel.ico')

        # ========== LABELFRAME ==========
        self.Labelframe1 = LabelFrame(root)
        self.Labelframe1.place(relx=0.01, rely=0.04, relheight=0.95, relwidth=0.97)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font17)
        self.Labelframe1.configure(text='Lista de hóspedes:')
        self.Labelframe1.configure(font=font17)
        self.Labelframe1.configure(background='#00868B')
        self.Labelframe1.configure(highlightbackground='#ffffff')
        self.Labelframe1.configure(highlightcolor='black')
        self.Labelframe1.configure(width=760)

        # ========== FRAMES ==========
        # Frame1 fica dentro do Labelframe1
        self.Frame1 = Frame(self.Labelframe1)
        self.Frame1.place(relx=0.03, rely=0.01, relheight=0.86, relwidth=0.47)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth='2')
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background='#FF8C69')
        self.Frame1.configure(highlightbackground='#ffffff')
        self.Frame1.configure(highlightcolor='black')
        self.Frame1.configure(width=355)

        # Frame2 fica dentro do Labelframe1
        self.Frame2 = Frame(self.Labelframe1)
        self.Frame2.place(relx=0.51, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth='2')
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background='#FF8C69')
        self.Frame2.configure(highlightbackground='#ffffff')
        self.Frame2.configure(highlightcolor='black')
        self.Frame2.configure(width=355)

        # ========== LABELS ==========
        # Label1 fica dentro do Frame1
        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.028, rely=0.02, height=37, width=117)
        self.Label1.configure(activebackground='#ffffff')
        self.Label1.configure(activeforeground='black')
        self.Label1.configure(background='#FF8C69')
        self.Label1.configure(disabledforeground='#a3a3a3')
        self.Label1.configure(font=font16)
        self.Label1.configure(foreground='#000000')
        self.Label1.configure(highlightbackground='#ffffff')
        self.Label1.configure(highlightcolor='black')
        self.Label1.configure(text='Nomes')

        # Label2 fica dentro do Frame2
        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.37, rely=0.02, height=44, width=156)
        self.Label2.configure(activebackground='#ffffff')
        self.Label2.configure(activeforeground='black')
        self.Label2.configure(background='#FF8C69')
        self.Label2.configure(disabledforeground='#a3a3a3')
        self.Label2.configure(font=font16)
        self.Label2.configure(foreground='#000000')
        self.Label2.configure(highlightbackground='#ffffff')
        self.Label2.configure(highlightcolor='black')
        self.Label2.configure(text='Quartos')

        # ========== TEXT BOX ==========
        # Text1 fica dentro do Frame1
        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.06, rely=0.16, relheight=0.08, relwidth=0.88)
        self.Text1.configure(background='white')
        self.Text1.configure(font=font16)
        self.Text1.configure(foreground='#000000')
        self.Text1.configure(highlightbackground='#d9d9d9')
        self.Text1.configure(highlightcolor='black')
        self.Text1.configure(insertbackground='black')
        self.Text1.configure(selectbackground='#c4c4c4')
        self.Text1.configure(selectforeground='black')
        self.Text1.configure(width=314)
        self.Text1.configure(wrap=WORD)

        # Text2 fica dentro do Frame2
        self.Text2 = Text(self.Frame1)
        self.Text2.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text2.configure(background='white')
        self.Text2.configure(font=font17)
        self.Text2.configure(foreground='black')
        self.Text2.configure(highlightbackground='#d9d9d9')
        self.Text2.configure(highlightcolor='black')
        self.Text2.configure(insertbackground='black')
        self.Text2.configure(selectbackground='#c4c4c4')
        self.Text2.configure(selectforeground='black')
        self.Text2.configure(width=314)
        self.Text2.configure(wrap=WORD)

        root.mainloop()


if __name__ == '__main__':
    hotel = HOTEL_MANAGEMENT_checkin()
