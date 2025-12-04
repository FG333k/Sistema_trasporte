from datetime import *
from sqlite3 import *

# Crialçaão da classe abstrata
class Trasporte:
    def __init__(self, tipo: str, tarifa_base: float, capacidade: int):

        # Atributos padrão
        self.tipo = tipo
        self.tarifa_base = tarifa_base
        self.capacidade = capacidade
        self.__velocidade_media = 0

    # Métodos get e set para o atributo privado
    def getVelocidade_media(self):
        return self.__velocidade_media
    
    def setVelocidade_media(self, valor):
        self.__velocidade_media = valor
        
    # Métodos padrão (abstratos) que devem ser implementdaos nas classes herdeiras
    def calcular_tarifa(self, distancia: float = 0, **kwargs) -> float: 
        return NotImplementedError("Deve ser implementado nas subclasses")

    def calcular_tempo_espera(self, hora_atual: datetime) -> timedelta:
        return NotImplementedError("Deve ser implementado nas subclasses")
    

class Onibus(Trasporte):
    # Método construtor com parametros pré-setados
    def __init__(self, tarifa_base: float = 4.50, capacidade: int = 34):
        # Super recebendo o tipo ingeçado, mas tarifa_base e capacidade do método construtor
        super().__init__("Ônibus", tarifa_base, capacidade)
        self.capacidade = capacidade
        self.__velocidade_media = 60

        # Atributo específico
        self.__intervalo_medio = timedelta(minutes=15)

    def getVelocidade_media(self):
        return self.__velocidade_media
    
    def setVelocidade_media(self, valor):
        self.__velocidade_media = valor

    def getIntervalo_medio(self):
        return self.__intervalo_medio

    def setIntervalo_medio(self, valor):
        self.__intervalo_medio = valor


    # Método para calcular o valor da tarifa
    def calcular_tarifa(self, distancia: float = 0, **kwargs) -> float:     # Não há necessidade de receber qualquer parametro pois o valor da tarifa é (fixa)
        self.tarifa = self.tarifa_base     #getTarifa_base()
        return self.tarifa

    def calcular_tempo_espera(self, hora_atual: datetime) -> timedelta:
        # Recebe a hora atual do sistema
        hora = hora_atual.hour

        # Verifica os intervalos de tempo para determinar (pico ou não)
        if(6 <= hora <= 9 or 16 <= hora <= 19):     # baixo fluxo
            return timedelta(minutes=5)
        elif(22 <= hora or hora <= 5):
            return timedelta(minutes=30)            # alto fluxo
        else:
            return self.getIntervalo_medio()             # fluxo médio


class Metro(Trasporte):
    def __init__(self, tarifa_base: float = 5.00, capacidade: int = 1200):
        super().__init__("Metrô", tarifa_base, capacidade)
        self.__velocidade_media = 100

        # Atributo específico
        self.__tarifa_por_km = 0.20
        
    def getVelocidade_media(self):
        return self.__velocidade_media
    
    def setVelocidade_media(self, valor):
        self.__velocidade_media = valor

    def getTarifa_por_km(self):
        return self.__tarifa_por_km

    def setTarifa_por_km(self, valor):
        self.__tarifa_por_km = valor

    def calcular_tarifa(self, distancia: float = 0, **kwargs) -> float: 
        if(distancia > 0):
            self.tarifa = ((self.getTarifa_por_km() * distancia) + self.tarifa_base)
            return self.tarifa
        else:
            return self.tarifa_base

    def calcular_tempo_espera(self, hora_atual: datetime) -> timedelta:
        hora = hora_atual.hour

        if(6 <= hora <= 9 or 16 <= hora <= 19):
            return timedelta(minutes=2)
        else:
            return timedelta(minutes=5)



class Trem(Trasporte):
    def __init__(self, tarifa_base: float = 6.5, capacidade: int = 500):
        super().__init__("Trem", tarifa_base, capacidade)
        self.__velocidade_media = 120

        # Atributo específico
        self.__tarifa_por_zona = 1.50

    def getVelocidade_media(self):
        return self.__velocidade_media
    
    def setVelocidade_media(self, valor):
        self.__velocidade_media = valor

    def getTarifa_por_zona(self):
        return self.__tarifa_por_zona
    
    def setTarifa_por_zona(self, valor):
        self.__tarifa_por_zona = valor

    def calcular_tarifa(self, distancia: float = 0, zonas: int = 1, **kwargs) -> float: 
        self.tarifa = (self.tarifa_base + (zonas * self.getTarifa_por_zona()))
        return self.tarifa

    def calcular_tempo_espera(self, hora_atual: datetime) -> timedelta:
        hora = hora_atual.hour

        if(6 <= hora <= 9 or 16 <= hora <= 19):
            return timedelta(minutes=8)
        else:
            return timedelta(minutes=15)

        

class Barco(Trasporte):
    def __init__(self, tarifa_base: float = 9.99, capacidade: int = 10):
        super().__init__("Barco", tarifa_base, capacidade)
        self.__velocidade_media = 80

        # Atributo específico
        self.__tarifa_por_trecho = 2.0

    def getVelocidade_media(self):
        return self.__velocidade_media
    
    def setVelocidade_media(self, valor):
        self.__velocidade_media = valor

    def getTarifa_por_trecho(self):
        return self.__tarifa_por_trecho
    
    def setTarifa_por_trecho(self, valor):
        self.__tarifa_por_trecho = valor

    def calcular_tarifa(self, distancia: float = 0, trechos: int = 1, **kwargs) -> float: 
        self.tarifa = (self.tarifa_base + (trechos * self.getTarifa_por_trecho()))
        return self.tarifa

    def calcular_tempo_espera(self, hora_atual: datetime) -> timedelta:
        hora = hora_atual.hour

        if(6 <= hora <= 9 or 16 <= hora <= 19):
            return timedelta(minutes=20)
        else:
            return timedelta(minutes=60)

# Tetativa de coneção ao banco de dados (para configrações ADM)
class Dados:
    def __init__(self):
        self.conn = connect('dados_trasnporte.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.verificar_tabela()

    def verificar_tabela(self):
        self.cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='transporte'
        """)

        verificacao_tabela = self.cursor.fetchone()

        if(not verificacao_tabela):
            self.cursor.execute("""
                CREATE TABLE transporte(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo VARHAR(40),
                    velocidade_nedia INTEGER,
                    tarifa_base FLOAT,
                    
                )
            """)


    def buscar_dados(self):
        pass

class Sistema_transporte:
    def __init__(self):
        # Dicionário com as intancias de cada veículo
        self.veiculos = {
            'onibus': Onibus(),
            'metro': Metro(),
            'trem': Trem(),
            'barco': Barco()
        }


    def calcular_viagem(self, tipo_veiculo: str, distancia: float = 0, **kwargs):
        # Verifica se o veículo é suportado
        if(tipo_veiculo not in self.veiculos):
            raise ValueError(f"Tipo de veículo não suportado: {tipo_veiculo}")
        
        # Pega o objeto deo veículo selecionádo
        veiculo = self.veiculos[tipo_veiculo]
        hora_atual = datetime.datetime.now()    # Obtem a hora atual

        # Calcula a tarifa e o tempo de espera usando o métodos polimorfos
        tarifa = veiculo.calcular_tarifa(distancia, **kwargs)
        tempo_espera = veiculo.calcular_tempo_espera(hora_atual)

        # Calcula tempo de viagem usando polimorfismo
        if(distancia > 0 and veiculo.getVelocidade_media() > 0):
            tempo_viagem = timedelta(hours=distancia / veiculo.getVelocidade_media())
        else:
            # Caso valores fiquem defaut
            tempo_viagem = timedelta(minutes=15)

        # calcular chegada estimada
        chegada_estimada = hora_atual + tempo_espera + tempo_viagem

        return {
            'veiculo': veiculo.tipo,
            'tarifa': tarifa,
            'tempo_espera': tempo_espera,
            'tempo_viagem': tempo_viagem,
            'chegada_estimada': chegada_estimada
        }