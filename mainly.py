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

    py3 = True


# função para iniciar a janela/página checkin_gui_and_program.py
def click_checkinn():
    call(["python", "checkin_gui_and_program.py"])


# função para iniciar a janela/página listgui.py
def click_list():
    call(["python", "listgui.py"])


# função para iniciar a janela/página checkoutgui.py
def click_checkout():
    call(["python", "checkoutgui.py"])


# função para iniciar a janela/página getinfoui.py
def click_getinfo():
    call(["python", "getinfoui.py"])


# cria a classe principal
class HOTEL_MANAGEMENT:
    def __init__(self):
        # inicia o root (tela principal)
        root = Tk()
        # configurações de fonte
        _bgcolor = 'd9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#ffffff'
        _ana1color = '#ffffff'
        _ana2color = '#ffffff'

        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        font14 = "-family {Segoe UI} -size 15 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"

        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"

        # configurações da tela principal
        root.geometry('923x640+540+110')
        root.title('Hotel Rafa Said')
        root.configure(background='#9ACD32')
        root.configure(highlightbackground='#d9d9d9')
        root.configure(highlightcolor='black')

        # ========== FRAMES ==========
        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth='2')
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background='darkseagreen')
        self.Frame1.configure(highlightbackground='#d9d9d9')
        self.Frame1.configure(highlightcolor='black')
        self.Frame1.configure(width=925)
        root.wm_iconbitmap(r'C:\\Users\\Usuario\\Documents\\Rafael\\Projetos\\Tkinter_poo\\icones\\hotel.ico')

        # ========== MESSAGES ==========
        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.00, rely=0.00, relheight=0.15, relwidth=1.00)
        self.Message6.configure(background='#40E0D0')
        self.Message6.configure(font=font14)
        self.Message6.configure(foreground='#008080')
        self.Message6.configure(highlightbackground='#d9d9d9')
        self.Message6.configure(highlightcolor='black')
        self.Message6.configure(text=''' Sistema Hotel - Sejam bem vindos ''')
        self.Message6.configure(width=880)

        # ========== BOTÕES ==========
        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.17, rely=0.17, height=90, width=566)
        # activebackground muda a cor de fundo do botão ao clicar nele
        self.Button2.configure(activebackground='#d9d9d9')
        self.Button2.configure(font=font14)
        self.Button2.configure(activeforeground='#000000')
        self.Button2.configure(background='cadetblue')
        self.Button2.configure(disabledforeground='#bfbfbf')
        self.Button2.configure(pady='0')
        self.Button2.configure(text='1 - Entrada')
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_checkinn)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.17, rely=0.33, height=90, width=566)
        # activebackground muda a cor de fundo do botão ao clicar nele
        self.Button3.configure(activebackground='#d9d9d9')
        self.Button3.configure(font=font14)
        self.Button3.configure(activeforeground='#000000')
        self.Button3.configure(background='skyblue')
        self.Button3.configure(disabledforeground='#bfbfbf')
        self.Button3.configure(pady='0')
        self.Button3.configure(text='2 - Mostrar lista convidados')
        self.Button3.configure(width=566)
        self.Button3.configure(command=click_list)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.17, rely=0.49, height=90, width=566)
        # activebackground muda a cor de fundo do botão ao clicar nele
        self.Button4.configure(activebackground='#d9d9d9')
        self.Button4.configure(font=font14)
        self.Button4.configure(activeforeground='#000000')
        self.Button4.configure(background='rosybrown')
        self.Button4.configure(disabledforeground='#bfbfbf')
        self.Button4.configure(pady='0')
        self.Button4.configure(text='3 - Saída')
        self.Button4.configure(width=566)
        self.Button4.configure(command=click_checkout)


        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.17, rely=0.65, height=90, width=566)
        # activebackground muda a cor de fundo do botão ao clicar nele
        self.Button5.configure(activebackground='#d9d9d9')
        self.Button5.configure(font=font14)
        self.Button5.configure(activeforeground='#000000')
        self.Button5.configure(background='powderblue')
        self.Button5.configure(disabledforeground='#bfbfbf')
        self.Button5.configure(pady='0')
        self.Button5.configure(text='4 - Informações do convidado')
        self.Button5.configure(width=566)
        self.Button5.configure(command=click_getinfo)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.17, rely=0.81, height=90, width=566)
        # activebackground muda a cor de fundo do botão ao clicar nele
        self.Button6.configure(activebackground='#d9d9d9')
        self.Button6.configure(font=font14)
        self.Button6.configure(activeforeground='#000000')
        self.Button6.configure(background='lightcoral')
        self.Button6.configure(disabledforeground='#bfbfbf')
        self.Button6.configure(pady='0')
        self.Button6.configure(text='5 - Sair')
        self.Button6.configure(width=566)
        self.Button6.configure(command=root.destroy)


        # executa o root
        root.mainloop()

# se a classe HOTEL_MANAGEMENT existir, chama o __main__
if __name__ == '__main__':
    GUEST = HOTEL_MANAGEMENT()