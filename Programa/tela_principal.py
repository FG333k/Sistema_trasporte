from main import *  
from tkinter import *
from tkinter import messagebox
import webbrowser

class Interface:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema de Transporte Público")
        self.janela.geometry("670x380")
        self.janela.resizable('false','false')
        self.janela.configure(background="#D6D6D6", padx=20, pady=20, )
        self.sistema = Sistema_transporte()
        self.entry_distancia = None
        self.spin_zonas = None
        self.spin_trechos = None

        self.iniciar()
        self.janela.mainloop()

    def iniciar(self):
        tela = Frame(self.janela)
        tela.configure(bg="#D6D6D6")
        tela.pack(fill=BOTH, expand=True)
        

        nome_programa = Label(
            tela,
            text="Sistema de Transporte Publico",
            bg="#D6D6D6"
        )
        nome_programa.pack(anchor="center", side="top")

        creditos = Button(
            tela,
            text="DEV by: Carlos Henrique - Felipe de Almeida",
            bg="#CCCCCC",
            command=self.abrir_repositorio,
            border=0
        )
        creditos.pack(anchor="se", side="bottom")

        # Frame à esquerda
        frame_esq = Frame(
            tela,
            width=290,
            height=290,
            bg="#D6D6D6"
        )
        frame_esq.pack(side="left", anchor="nw")
        # Cansei nesse kkkkkkk

        # #
        # Fundo da seção principal do frame da esquerda
        back_sec_principal = Frame(frame_esq, width=290, height=130, bg="#ffffff" )
        back_sec_principal.place(x=0, y=0)

        # ##
        # Nome da seção principal
        nome_sec = Label(back_sec_principal, text="Selecione o tipo de transporte", bg="#ffffff")
        nome_sec.place(x=10, y=0)

        # ##
        # Bloco da sessão prinipal
        bloco_sessao_primaria = Frame(back_sec_principal, width=290, height=110, padx=5, pady=5, border=0.5, bg="#ffffff", relief='solid',borderwidth=1)
        bloco_sessao_primaria.place(x=0, y=20)

        # ###
        # Formatação interna do bloco
        bloco_int = Frame(bloco_sessao_primaria, width=270, height=90, bg="#D6D6D6")
        bloco_int.place(x=5, y=5)

        # ####
        # Radio butons e labels relativas
        self.transporte_selecionado = StringVar(value='onibus')

        radio_onibus = Radiobutton(bloco_int, text="Ônibus", bg="#D6D6D6", variable=self.transporte_selecionado, value="onibus", activebackground="#D6D6D6", command=self.mostrar_campos_adicionais)
        radio_onibus.place(x=5, y=5)
        tarifa_onibus = Label(bloco_int, text=f"Tarifa:    (Fixa) R$ {self.sistema.veiculos['onibus'].calcular_tarifa():.2f}", bg="#D6D6D6")
        tarifa_onibus.place(x=95, y=7)

        radio_metro = Radiobutton(bloco_int, text="Metrô", bg="#D6D6D6", variable=self.transporte_selecionado, value="metro", activebackground="#D6D6D6", command=self.mostrar_campos_adicionais)
        radio_metro.place(x=5, y=25)
        tarifa_metro = Label(bloco_int, text=f"Tarifa:    (base) + por distancia", bg="#D6D6D6")
        tarifa_metro.place(x=95, y=27)

        radio_trem = Radiobutton(bloco_int, text="Trem", bg="#D6D6D6", variable=self.transporte_selecionado, value="trem", activebackground="#D6D6D6", command=self.mostrar_campos_adicionais)
        radio_trem.place(x=5, y=45)
        tarifa_trem = Label(bloco_int, text="Tarifa:    Por zonas", bg="#D6D6D6")
        tarifa_trem.place(x=95, y=47)

        radio_barco = Radiobutton(bloco_int, text="Barco", bg="#D6D6D6", variable=self.transporte_selecionado, value="barco", activebackground="#D6D6D6", command=self.mostrar_campos_adicionais)
        radio_barco.place(x=5, y=65)
        tarifa_barco = Label(bloco_int, text="Tarifa:    Por trechos", bg="#D6D6D6")
        tarifa_barco.place(x=95, y=67)


        # #
        # Fundo da seção de notas
        bloco_sessao_notas = Frame(frame_esq, width=290, height=80, padx=15, pady=2, bg="#B8EBB8", relief="solid",borderwidth=1)
        bloco_sessao_notas.place(x=0, y=140)

        # ##
        # Titulo das notas
        titulo_notas = Label(bloco_sessao_notas, text="NOTA Os cálculos consideram:", bg="#B8EBB8")
        titulo_notas.place(x=0, y=0)

        # ##
        # Considerações
        c1 = Label(bloco_sessao_notas, text="° Horário de pico", bg="#B8EBB8")
        c1.place(x=0, y=20)

        # ##
        c1 = Label(bloco_sessao_notas, text="° Velocidade média do veículo", bg="#B8EBB8")
        c1.place(x=0, y=35)

        # ##
        c1 = Label(bloco_sessao_notas, text="° Tarifas especificas de cada transporte", bg="#B8EBB8")
        c1.place(x=0, y=50)

        # 
        # Frame para campos variáveis
        self.frame_campos_variaveis = Frame(frame_esq, width=270, height=50, bg="#F0F0F0")
        self.frame_campos_variaveis.place(x=10, y=220)

        self.mostrar_campos_adicionais()

        # #
        # Botão para calcular a viagem
        self.calc_btn = Button(frame_esq, text="Calcular Viagem", width=15, height=1, bg="#A3A3A3", command=self.calcular_viagem, relief="solid",borderwidth=1)   
        self.calc_btn.place(x=80, y=260)
            

        # Frame à direita
        frame_dir = Frame(tela, width=290, height=260, bg="#ffffff")
        frame_dir.pack(anchor="ne", side="right")

        # #
        # Nome da sessão
        nome_sec = Label(frame_dir, text="Dados da Viagem", bg="#ffffff")
        nome_sec.place(x=10, y=0)

        # #
        # Fundo da sessão
        back_sec = Frame(frame_dir, width=290, height=145, border=1, bg="#ffffff", relief="solid",borderwidth=1)
        back_sec.place(x=0, y=20)

        # ##
        # Fromatação do fundo da sessão
        bloco_back = Frame(back_sec, width=265, height=130, bg="#D6D6D6")
        bloco_back.place(x=12, y=12)

        # ###
        # Labels de dados
        self.label_veiculo = Label(bloco_back, text="Veículo:", bg="#D6D6D6")
        self.label_veiculo.place(x=10, y=5)
        self.lbl_dado_veiculo = Label(bloco_back, text="---", bg="#D6D6D6")
        self.lbl_dado_veiculo.place(x=150, y=5)

        self.label_tarifa = Label(bloco_back, text="Tarifa:", bg="#D6D6D6")
        self.label_tarifa.place(x=10, y=30)
        self.lbl_dado_tarifa = Label(bloco_back, text="R$ 0.00", bg="#D6D6D6")
        self.lbl_dado_tarifa.place(x=150, y=30)

        self.label_tempEspera = Label(bloco_back, text="Tempo de espera:", bg="#D6D6D6")
        self.label_tempEspera.place(x=10, y=55)
        self.lbl_dado_tempEspera = Label(bloco_back, text="0 minutos", bg="#D6D6D6")
        self.lbl_dado_tempEspera.place(x=150, y=55)

        self.label_tempViagem = Label(bloco_back, text="Tempo de viagem:", bg="#D6D6D6")
        self.label_tempViagem.place(x=10, y=80)
        self.lbl_dado_tempViagem = Label(bloco_back, text="0 minutos", bg="#D6D6D6")
        self.lbl_dado_tempViagem.place(x=150, y=80)

        self.label_chegEstimada = Label(bloco_back, text="Chegada estimada:", bg="#D6D6D6")
        self.label_chegEstimada.place(x=10, y=105)
        self.lbl_dado_chegEstimada = Label(bloco_back, text="--:--", bg="#D6D6D6")
        self.lbl_dado_chegEstimada.place(x=150, y=105)

        # #
        # Fundo da subsessão
        back_sub = Frame(frame_dir, width=290, height=95, border=1,  bg="#ffffff",relief="solid",borderwidth=1)
        back_sub.place(x=0, y=165)

        # ##
        # Título da dubsessão
        nome_sub = Label(back_sub, text="Comparação rápida", bg="#ffffff")
        nome_sub.place(x=10, y=0)

        # ###
        # Formatação interna da subsessão
        bloco_sub = Frame(back_sub, width=265, height=60, background="#D6D6D6")
        bloco_sub.place(x=12, y=20)

        # ####
        # Botão de comparação
        compar_btn = Button(bloco_sub, width=20, height=1, text="Comparar Todas as Tarifas", command=self.comparar,relief="solid",borderwidth=1,bg="#A3A3A3")
        compar_btn.place(x=60, y=18)

    def mostrar_campos_adicionais(self):


        for dado in self.frame_campos_variaveis.winfo_children():
            dado.destroy()

        trasnporte = self.transporte_selecionado.get()

        if(trasnporte == 'metro'):
            Label(self.frame_campos_variaveis, text="Distancia            (km):", bg="#F0F0F0").place(x=65, y=5)
            self.entry_distancia = Entry(self.frame_campos_variaveis, width=10)
            self.entry_distancia.place(x=120, y=5)
            self.entry_distancia.insert(0, "10")

        elif(trasnporte == 'trem'):
            Label(self.frame_campos_variaveis, text="Zonas:", bg="#F0F0F0").place(x=80, y=5)
            self.spin_zonas = Spinbox(self.frame_campos_variaveis, from_=1, to=10, width=5)
            self.spin_zonas.place(x=120, y=5)
            self.spin_zonas.delete(0, END)
            self.spin_zonas.insert(0, "3")

        elif(trasnporte == 'barco'):
            Label(self.frame_campos_variaveis, text="Trechos:", bg="#F0F0F0").place(x=80, y=5)
            self.spin_trechos = Spinbox(self.frame_campos_variaveis, from_=1, to=10, width=5)
            self.spin_trechos.place(x=130, y=5)
            self.spin_trechos.delete(0, END)
            self.spin_trechos.insert(0, "2")

    def calcular_viagem(self):
        try:
            transporte = self.transporte_selecionado.get()

            parametros_extras = {}
            distancia = 0
            zonas = ""

            if(transporte == 'metro'):
                if(self.entry_distancia):
                    distancia = float(self.entry_distancia.get())
            
            elif(transporte == 'trem'):
                if(self.spin_zonas):
                    parametros_extras['zonas'] = int(self.spin_zonas.get())

            elif(transporte == 'barco'):
                if(self.spin_trechos):
                    parametros_extras['trechos'] = int(self.spin_trechos.get())
                
            resultado = self.sistema.calcular_viagem(transporte, distancia, **parametros_extras)

            self.atualizar_resultados(resultado)

        except ValueError:
            messagebox.showerror("Erro:", "Por favor, insira valores válidos.")

        except Exception as e:
            messagebox.showerror("Erro:", f"Ocorreu um erro {str(e)}")
            

    def atualizar_resultados(self, resultado):

        
        self.lbl_dado_veiculo.config(text=resultado['veiculo'])
        self.lbl_dado_tarifa.config(text=f"R$ {resultado['tarifa']:.2f}")
        self.lbl_dado_tempEspera.config(text=f"{resultado['tempo_espera'].seconds //60} minutos")
        self.lbl_dado_tempViagem.config(text=f"{resultado['tempo_viagem'].seconds //60} minutos")
        self.lbl_dado_chegEstimada.config(text=resultado['chegada_estimada'].strftime('%H:%M'))



    def abrir_repositorio(self):
        webbrowser.open_new("https://github.com/FG333k/Sistema_trasporte")


    # Janela da tabela de comparação
    def comparar(self):
        janela_comparacao = Toplevel(self.janela)
        from tela_comparacao_tarif import Application
        Application(janela_comparacao)

janela = Tk()
aplicacao = Interface(janela)