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

        font11 = '-family {Segoe UI} -size 11 -weight normal -slant ' \
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

        font30 = '-family {Segoe UI} -size 30 -weight bold -slant ' \
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
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=WORD)

        # ========== FRAMES ==========
        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth='2')
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background='#FF3E96')
        self.Frame1.configure(highlightbackground='#ffffff')
        self.Frame1.configure(highlightcolor='black')
        self.Frame1.configure(width=995)

        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.03, rely=0.18, relheight=0.46, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth='2')
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background='#00EE76')
        self.Frame2.configure(highlightbackground='#ffffff')
        self.Frame2.configure(highlightcolor='black')
        self.Frame2.configure(width=995)

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

        self.Message4 = Message(self.Frame2)
        self.Message4.place(relx=0.41, rely=0.04, relheight=0.1, relwidth=0.05)
        self.Message4.configure(background='#00EE76')
        self.Message4.configure(font=font13)
        self.Message4.configure(foreground='#000000')
        self.Message4.configure(highlightbackground='#ffffff')
        self.Message4.configure(highlightcolor='black')
        self.Message4.configure(text=':')
        self.Message4.configure(width=46)

        self.Message5 = Message(self.Frame2)
        self.Message5.place(relx=0.42, rely=0.17, relheight=0.12, relwidth=0.03)
        self.Message5.configure(background='#00EE76')
        self.Message5.configure(font=font13)
        self.Message5.configure(foreground='#000000')
        self.Message5.configure(highlightbackground='#ffffff')
        self.Message5.configure(highlightcolor='black')
        self.Message5.configure(text=':')
        self.Message5.configure(width=26)

        self.Message6 = Message(self.Frame2)
        self.Message6.place(relx=0.415, rely=0.3, relheight=0.09, relwidth=0.04)
        self.Message6.configure(background='#00EE76')
        self.Message6.configure(font=font13)
        self.Message6.configure(foreground='#000000')
        self.Message6.configure(highlightbackground='#ffffff')
        self.Message6.configure(highlightcolor='black')
        self.Message6.configure(text=':')
        self.Message6.configure(width=36)

        self.Message7 = Message(self.Frame2)
        self.Message7.place(relx=0.05, rely=0.55, relheight=0.15, relwidth=0.600)
        self.Message7.configure(background='#00EE76')
        self.Message7.configure(font=font13)
        self.Message7.configure(foreground='#000000')
        self.Message7.configure(highlightbackground='#ffffff')
        self.Message7.configure(highlightcolor='black')
        self.Message7.configure(text='-')
        self.Message7.configure(width=41)

        self.Message8 = Message(self.Frame2)
        self.Message8.place(relx=0.42, rely=0.41, relheight=0.11, relwidth=0.03)
        self.Message8.configure(background='#00EE76')
        self.Message8.configure(font=font13)
        self.Message8.configure(foreground='#000000')
        self.Message8.configure(highlightbackground='#ffffff')
        self.Message8.configure(highlightcolor='black')
        self.Message8.configure(text=':')
        self.Message8.configure(width=26)

        # ========== LABELS ==========
        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.033, rely=0.43, height=44, width=260)
        self.Label1.configure(activebackground='#ffffff')
        self.Label1.configure(activeforeground='black')
        self.Label1.configure(background='#00EE76')
        self.Label1.configure(disabledforeground='#bfbfbf')
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground='#000000')
        self.Label1.configure(highlightbackground='#ffffff')
        self.Label1.configure(highlightcolor='black')
        self.Label1.configure(text='Número de dias')

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.05, rely=0.03, height=40, width=289)
        self.Label3.configure(activebackground='#ffffff')
        self.Label3.configure(activeforeground='black')
        self.Label3.configure(background='#00EE76')
        self.Label3.configure(disabledforeground='#bfbfbf')
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground='#000000')
        self.Label3.configure(highlightbackground='#ffffff')
        self.Label3.configure(highlightcolor='black')
        self.Label3.configure(text='Nome do cliente')

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.022, rely=0.29, height=40, width=329)
        self.Label4.configure(activebackground='#ffffff')
        self.Label4.configure(activeforeground='black')
        self.Label4.configure(background='#00EE76')
        self.Label4.configure(disabledforeground='#bfbfbf')
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground='#000000')
        self.Label4.configure(highlightbackground='#ffffff')
        self.Label4.configure(highlightcolor='black')
        self.Label4.configure(text='Digite telefone')

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.022, rely=0.16, height=40, width=334)
        self.Label5.configure(activebackground='#ffffff')
        self.Label5.configure(activeforeground='black')
        self.Label5.configure(background='#00EE76')
        self.Label5.configure(disabledforeground='#bfbfbf')
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground='#000000')
        self.Label5.configure(highlightbackground='#ffffff')
        self.Label5.configure(highlightcolor='black')
        self.Label5.configure(text='Digite Endereço')

        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.32, rely=0.5, height=48, width=296)
        self.Label6.configure(activebackground='#ffffff')
        self.Label6.configure(activeforeground='black')
        self.Label6.configure(background='#00EE76')
        self.Label6.configure(disabledforeground='#bfbfbf')
        self.Label6.configure(font=font12)
        self.Label6.configure(foreground='#000000')
        self.Label6.configure(highlightbackground='#ffffff')
        self.Label6.configure(highlightcolor='black')
        self.Label6.configure(text='Escolha o quarto')

        self.Label7 = Label(self.Frame2)
        self.Label7.place(relx=0.20, rely=0.79, height=48, width=300)
        self.Label7.configure(activebackground='#ffffff')
        self.Label7.configure(activeforeground='black')
        self.Label7.configure(background='#00EE76')
        self.Label7.configure(disabledforeground='#bfbfbf')
        self.Label7.configure(font=font11)
        self.Label7.configure(foreground='#000000')
        self.Label7.configure(highlightbackground='#ffffff')
        self.Label7.configure(highlightcolor='black')
        self.Label7.configure(text='Forma de pagamento')

        # ========== ENTRY ==========
        self.Entry1 = Entry(self.Frame2)
        self.Entry1.place(relx=0.47, rely=0.43, height=34, relwidth=0.43)
        self.Entry1.configure(background='white')
        self.Entry1.configure(disabledforeground='#bfbfbf')
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground='#000000')
        self.Entry1.configure(highlightbackground='#ffffff')
        self.Entry1.configure(highlightcolor='black')
        self.Entry1.configure(insertbackground='black')
        self.Entry1.configure(selectbackground='#e6e6e6')
        self.Entry1.configure(selectforeground='black')
        self.Entry1.configure(width=424)

        self.Entry3 = Entry(self.Frame2)
        self.Entry3.place(relx=0.47, rely=0.05, height=34, relwidth=0.43)
        self.Entry3.configure(background='white')
        self.Entry3.configure(disabledforeground='#bfbfbf')
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground='#000000')
        self.Entry3.configure(highlightbackground='#ffffff')
        self.Entry3.configure(highlightcolor='black')
        self.Entry3.configure(insertbackground='black')
        self.Entry3.configure(selectbackground='#e6e6e6')
        self.Entry3.configure(selectforeground='black')

        self.Entry4 = Entry(self.Frame2)
        self.Entry4.place(relx=0.47, rely=0.31, height=34, relwidth=0.43)
        self.Entry4.configure(background='white')
        self.Entry4.configure(disabledforeground='#bfbfbf')
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground='#000000')
        self.Entry4.configure(highlightbackground='#ffffff')
        self.Entry4.configure(highlightcolor='black')
        self.Entry4.configure(insertbackground='black')
        self.Entry4.configure(selectbackground='#e6e6e6')
        self.Entry4.configure(selectforeground='black')

        self.Entry5 = Entry(self.Frame2)
        self.Entry5.place(relx=0.47, rely=0.18, height=34, relwidth=0.43)
        self.Entry5.configure(background='white')
        self.Entry5.configure(disabledforeground='#bfbfbf')
        self.Entry5.configure(font=font10)
        self.Entry5.configure(foreground='#000000')
        self.Entry5.configure(highlightbackground='#ffffff')
        self.Entry5.configure(highlightcolor='black')
        self.Entry5.configure(insertbackground='black')
        self.Entry5.configure(selectbackground='#e6e6e6')
        self.Entry5.configure(selectforeground='black')

        # ========== CHECKBOX ==========
        self.Checkbutton1 = Checkbutton(self.Frame2)
        self.Checkbutton1.place(relx=0.08, rely=0.63, relheight=0.17, relwidth=0.14)
        self.Checkbutton1.configure(activebackground='#ffffff')
        self.Checkbutton1.configure(activeforeground='#000000')
        self.Checkbutton1.configure(background='#00EE76')
        self.Checkbutton1.configure(disabledforeground='#bfbfbf')
        self.Checkbutton1.configure(font=font11)
        self.Checkbutton1.configure(foreground='#000000')
        self.Checkbutton1.configure(highlightbackground='#ffffff')
        self.Checkbutton1.configure(highlightcolor='black')
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='Luxo')

        self.Checkbutton2 = Checkbutton(self.Frame2)
        self.Checkbutton2.place(relx=0.08, rely=0.74, relheight=0.11, relwidth=0.21)
        self.Checkbutton2.configure(activebackground='#ffffff')
        self.Checkbutton2.configure(activeforeground='#000000')
        self.Checkbutton2.configure(background='#00EE76')
        self.Checkbutton2.configure(disabledforeground='#bfbfbf')
        self.Checkbutton2.configure(font=font11)
        self.Checkbutton2.configure(foreground='#000000')
        self.Checkbutton2.configure(highlightbackground='#ffffff')
        self.Checkbutton2.configure(highlightcolor='black')
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='Luxo completo')

        self.Checkbutton3 = Checkbutton(self.Frame2)
        self.Checkbutton3.place(relx=0.47, rely=0.75, relheight=0.11, relwidth=0.16)
        self.Checkbutton3.configure(activebackground='#ffffff')
        self.Checkbutton3.configure(activeforeground='#000000')
        self.Checkbutton3.configure(background='#00EE76')
        self.Checkbutton3.configure(disabledforeground='#bfbfbf')
        self.Checkbutton3.configure(font=font11)
        self.Checkbutton3.configure(foreground='#000000')
        self.Checkbutton3.configure(highlightbackground='#ffffff')
        self.Checkbutton3.configure(highlightcolor='black')
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='Geral')

        self.Checkbutton4 = Checkbutton(self.Frame2)
        self.Checkbutton4.place(relx=0.5, rely=0.67, relheight=0.11, relwidth=0.12)
        self.Checkbutton4.configure(activebackground='#ffffff')
        self.Checkbutton4.configure(activeforeground='#000000')
        self.Checkbutton4.configure(background='#00EE76')
        self.Checkbutton4.configure(disabledforeground='#bfbfbf')
        self.Checkbutton4.configure(font=font11)
        self.Checkbutton4.configure(foreground='#000000')
        self.Checkbutton4.configure(highlightbackground='#ffffff')
        self.Checkbutton4.configure(highlightcolor='black')
        self.Checkbutton4.configure(justify=LEFT)
        self.Checkbutton4.configure(text='Conjunto')

        self.Checkbutton5 = Checkbutton(self.Frame2)
        self.Checkbutton5.place(relx=0.400, rely=0.89, relheight=0.1, relwidth=0.3)
        self.Checkbutton5.configure(activebackground='#ffffff')
        self.Checkbutton5.configure(activeforeground='#000000')
        self.Checkbutton5.configure(background='#00EE76')
        self.Checkbutton5.configure(disabledforeground='#bfbfbf')
        self.Checkbutton5.configure(font=font11)
        self.Checkbutton5.configure(foreground='#000000')
        self.Checkbutton5.configure(highlightbackground='#ffffff')
        self.Checkbutton5.configure(highlightcolor='black')
        self.Checkbutton5.configure(justify=LEFT)
        self.Checkbutton5.configure(text='Cartão de crédito/débito')

        self.Checkbutton6 = Checkbutton(self.Frame2)
        self.Checkbutton6.place(relx=0.200, rely=0.89, relheight=0.1, relwidth=0.15)
        self.Checkbutton6.configure(activebackground='#ffffff')
        self.Checkbutton6.configure(activeforeground='#000000')
        self.Checkbutton6.configure(background='#00EE76')
        self.Checkbutton6.configure(disabledforeground='#bfbfbf')
        self.Checkbutton6.configure(font=font11)
        self.Checkbutton6.configure(foreground='#000000')
        self.Checkbutton6.configure(highlightbackground='#ffffff')
        self.Checkbutton6.configure(highlightcolor='black')
        self.Checkbutton6.configure(justify=LEFT)
        self.Checkbutton6.configure(text='Dinheiro')

        # ========== BOTÕES ==========
        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.91, rely=0.05, height=33, width=43)
        self.Button1.configure(activebackground='#ffffff')
        self.Button1.configure(activeforeground='#000000')
        self.Button1.configure(background='#FF4500')
        self.Button1.configure(disabledforeground='#bfbfbf')
        self.Button1.configure(foreground='#FFFF00')
        self.Button1.configure(highlightbackground='#ffffff')
        self.Button1.configure(highlightcolor='black')
        self.Button1.configure(pady='0')
        self.Button1.configure(text='OK')

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.18, height=33, width=43)
        self.Button2.configure(activebackground='#ffffff')
        self.Button2.configure(activeforeground='#000000')
        self.Button2.configure(background='#FF4500')
        self.Button2.configure(disabledforeground='#bfbfbf')
        self.Button2.configure(foreground='#FFFF00')
        self.Button2.configure(highlightbackground='#ffffff')
        self.Button2.configure(highlightcolor='black')
        self.Button2.configure(pady='0')
        self.Button2.configure(text='OK')

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.91, rely=0.31, height=33, width=43)
        self.Button3.configure(activebackground='#ffffff')
        self.Button3.configure(activeforeground='#000000')
        self.Button3.configure(background='#FF4500')
        self.Button3.configure(disabledforeground='#bfbfbf')
        self.Button3.configure(foreground='#FFFF00')
        self.Button3.configure(highlightbackground='#ffffff')
        self.Button3.configure(highlightcolor='black')
        self.Button3.configure(pady='0')
        self.Button3.configure(text='OK')

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.76, rely=0.66, height=83, width=156)
        self.Button4.configure(activebackground='#ffffff')
        self.Button4.configure(activeforeground='#000000')
        self.Button4.configure(background='#FF4500')
        self.Button4.configure(disabledforeground='#bfbfbf')
        self.Button4.configure(foreground='#FFFF00')
        self.Button4.configure(highlightbackground='#ffffff')
        self.Button4.configure(highlightcolor='black')
        self.Button4.configure(pady='0')
        self.Button4.configure(text='OK')

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.91, rely=0.43, height=33, width=43)
        self.Button5.configure(activebackground='#ffffff')
        self.Button5.configure(activeforeground='#000000')
        self.Button5.configure(background='#FF4500')
        self.Button5.configure(disabledforeground='#bfbfbf')
        self.Button5.configure(foreground='#FFFF00')
        self.Button5.configure(highlightbackground='#ffffff')
        self.Button5.configure(highlightcolor='black')
        self.Button5.configure(pady='0')
        self.Button5.configure(text='OK')

        root.mainloop()


if __name__ == '__main__':
    hotel = HOTEL_MANAGEMENT_checkin()
