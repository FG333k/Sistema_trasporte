import main
from tkinter import *

janela = Tk()

class Application():
    def __init__(self,janela):
            self.sistem = main.Sistema_transporte()
            self.janela = janela
            self.tela()
            self.textTela()
            self.frameTela()
            janela.mainloop()

    def tela(self):
            self.janela.title("Comparação de Tarifas",)
            self.janela.geometry('700x500')
            self.janela.resizable('false','false')

    def textTela(self):
            self.titulo = Label(self.janela, text="Comparação de Tarifas Por Transporte", font=("Arial",20,"bold"),height=2,width=50)  
            self.titulo.place( x=-91 , y=36 )
            self.nota = Label(self.janela, text="Tempo de espera varia conforme horário pico/fora de pico", font=("impact",10))
            self.nota.place(x=180,y=465)

    def frameTela(self):
            self.frame_1 = Frame(self.janela, bd=2, highlightbackground= 'black' , highlightthickness=1.5)
            self.frame_1.place(relx=0.04,rely=0.25 , relwidth=0.91, relheight=0.45 )
            # Labels filhas do Frame_1
            self.textFrame = Label(self.frame_1, text="Transporte",relief="solid", highlightbackground= 'blue', bd=2, bg= "#CECBCB")
            self.textFrame.place(relx=0.01, rely=0.01, relwidth=0.23, relheight=0.09)
            self.textFrame = Label(self.frame_1, text="Tarifa Base",relief="solid", highlightbackground= 'blue', bd=2, bg= "#CECBCB")
            self.textFrame.place(relx=0.27, rely=0.01, relwidth=0.19, relheight=0.09)
            self.textFrame = Label(self.frame_1, text="Exemplo Prático",relief="solid", highlightbackground= 'blue', bd=2, bg= "#CECBCB")
            self.textFrame.place(relx=0.54, rely=0.01, relwidth=0.19, relheight=0.09)
            self.textFrame = Label(self.frame_1, text="Tempo Espera",relief="solid", highlightbackground= 'blue', bd=2, bg= "#CECBCB")
            self.textFrame.place(relx=0.80, rely=0.01, relwidth=0.19, relheight=0.09)
            # linhas entre os Label
            self.linha_1 = Frame(self.frame_1, bg="black")
            self.linha_1.place(relx=0.25, rely=0.04, width=1, relheight=1)
            self.linha_2 = Frame(self.frame_1, bg="black")
            self.linha_2.place(relx=0.50, rely=0.04, width=1, relheight=1)
            self.linha_3 = Frame(self.frame_1, bg="black")
            self.linha_3.place(relx=0.76, rely=0.04, width=1, relheight=1)

            # textos entre as linhas (textos abaixo de Transporte)
            self.texto = Label(self.frame_1, text="Ônibus")
            self.texto.place(relx=0.01, rely=0.14, relwidth=0.1, relheight=0.1)
            self.texto = Label(self.frame_1, text="Metrô")
            self.texto.place(relx=0.01, rely=0.24, relwidth=0.1, relheight=0.1)
            self.texto = Label(self.frame_1, text="Trem")
            self.texto.place(relx=0.01, rely=0.35, relwidth=0.1, relheight=0.1)
            self.texto = Label(self.frame_1, text="Barco")
            self.texto.place(relx=0.01, rely=0.48, relwidth=0.1, relheight=0.1)

            # abaixo de Tarifa Base
            self.texto = Label(self.frame_1, text=F"  R$ {self.sistem.veiculos['onibus'].calcular_tarifa()}", font=("Times",10),fg="black")
            self.texto.place(relx=0.26, rely=0.11, relwidth=0.1, relheight=0.1)
            self.texto = Label(self.frame_1, text=F"  R$ {self.sistem.veiculos['metro'].calcular_tarifa()}", font=("Times",10),fg="black")
            self.texto.place(relx=0.26, rely=0.22, relwidth=0.1, relheight=0.1)
            self.texto = Label(self.frame_1, text=F"  R$ {self.sistem.veiculos['trem'].calcular_tarifa(0)}", font=("Times",10),fg="black")
            self.texto.place(relx=0.26, rely=0.35, relwidth=0.1, relheight=0.1)
            self.texto = Label(self.frame_1, text=F"  R$ {self.sistem.veiculos['barco'].calcular_tarifa(0)}", font=("Times",10),fg="black")
            self.texto.place(relx=0.26, rely=0.48, relwidth=0.1, relheight=0.1)

            # Abaixo da Exemplo Prático
            distancia_metro = 10
            zonas = 3
            trecho = 7
            self.texto = Label(self.frame_1, text="Qualquer Distacia", font=("Times",10),fg="black")
            self.texto.place(relx=0.52, rely=0.11, relwidth=0.2, relheight=0.1)
            self.texto = Label(self.frame_1, text= f"R$ {self.sistem.veiculos['metro'].calcular_tarifa(distancia_metro):.2f} ({distancia_metro}Km)", font=("Times",10),fg="black")
            self.texto.place(relx=0.51, rely=0.22, relwidth=0.2, relheight=0.1)
            self.texto = Label(self.frame_1, text= f"R$ {self.sistem.veiculos['trem'].calcular_tarifa(zonas):.2f} ({zonas} zonas)", font=("Times",10),fg="black")
            self.texto.place(relx=0.52, rely=0.35, relwidth=0.2, relheight=0.1)
            self.texto = Label(self.frame_1, text= f"R$ {self.sistem.veiculos['barco'].calcular_tarifa(trecho):.2f} ({trecho} trechos)", font=("Times",10),fg="black")
            self.texto.place(relx=0.52, rely=0.48, relwidth=0.2, relheight=0.1)

            # Abaixo do tempo Espera
            self.texto = Label(self.frame_1, text="5-30 min", font=("Times",10),fg="black")
            self.texto.place(relx=0.80, rely=0.11, relwidth=0.07, relheight=0.1)
            self.texto = Label(self.frame_1, text="2-5 min", font=("Times",10),fg="black")
            self.texto.place(relx=0.80, rely=0.22, relwidth=0.07, relheight=0.1)
            self.texto = Label(self.frame_1, text="8-15 min", font=("Times",10),fg="black")
            self.texto.place(relx=0.80, rely=0.35, relwidth=0.07, relheight=0.1)
            self.texto = Label(self.frame_1, text="20-60 min", font=("Times",10),fg="black")
            self.texto.place(relx=0.80, rely=0.48, relwidth=0.09, relheight=0.1)















Application(janela)
