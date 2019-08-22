import os
import pickle
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


# classe para fazer o checkout
class New_Toplevel:
    def __init__(self):
        root = Tk()
        # configurações de fonte
        _bgcolor = 'ffffff'
        _fgcolor = '#000000'
        _compcolor = '#ffffff'
        _ana1color = '#ffffff'
        _ana2color = '#ffffff'

        font9 = '-family {Segoe UI} -size 9 -weight normal -slant ' \
                'roman -underline 0 -overstrike 0'

        font10 = '-family {Courier New} -size 10 -weight bold -slant ' \
                 'roman -underline 0 -overstrike 0'

        # font11
        font23 = '-family {Segoe UI} -size 23 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        # font12
        font24 = '-family {Segoe UI} -size 24 -weight normal -slant ' \
                 'roman -underline 0 -overstrike 0'

        # configurações da tela principal
        root.geometry('1011x500')
        root.title('Hotel Rafa Said')
        root.configure(background='darkgreen')
        root.configure(highlightbackground='#ffffff')
        root.configure(highlightcolor='black')
        root.wm_iconbitmap(r'icones/hotel.ico')

        # ========== FRAMES ==========
        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.04, rely=0.04, relheight=0.91, relwidth=0.91)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth='2')
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background='darkseagreen')
        self.Frame1.configure(highlightbackground='#ffffff')
        self.Frame1.configure(highlightcolor='black')
        self.Frame1.configure(width=995)

        # ========== LABELS ==========
        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.14, rely=0.12, height=46, width=442)
        self.Label1.configure(activebackground='#ffffff')
        self.Label1.configure(activeforeground='black')
        self.Label1.configure(background='darkseagreen')
        self.Label1.configure(disabledforeground='#bfbfbf')
        self.Label1.configure(font=font23)
        self.Label1.configure(foreground='#000000')
        self.Label1.configure(highlightbackground='#ffffff')
        self.Label1.configure(highlightcolor='black')
        self.Label1.configure(text='Digite o nº quarto: ')

        # ========== ENTRYS ==========
        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.67, rely=0.12, height=44, relwidth=0.07)
        self.Entry1.configure(background='white')
        self.Entry1.configure(disabledforeground='#bfbfbf')
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground='#000000')
        self.Entry1.configure(highlightbackground='#ffffff')
        self.Entry1.configure(highlightcolor='black')
        self.Entry1.configure(insertbackground='black')
        self.Entry1.configure(selectbackground='#e6e6e6')
        self.Entry1.configure(selectforeground='black')

        # ========== TEXT BOX ==========
        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.05, rely=0.54, relheight=0.04, relwidth=0.89)
        self.Text1.configure(background='white')
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground='black')
        self.Text1.configure(highlightbackground='#ffffff')
        self.Text1.configure(highlightcolor='black')
        self.Text1.configure(insertbackground='black')
        self.Text1.configure(selectbackground='#e6e6e6')
        self.Text1.configure(selectforeground='black')
        self.Text1.configure(width=824)
        self.Text1.configure(wrap=WORD)

        root.mainloop()


if __name__ == '__main__':
    out = New_Toplevel()
