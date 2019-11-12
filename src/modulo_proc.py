from threading import Thread
import operator

class Process:
    def __init__(self, process):
        self.tempo_init = process[0]
        self.prioridade = process[1]
        self.tempo_processador = process[2]
        self.blocos_memoria = process[3]
        self.numero_impressora = process[4]
        self.requisicao_scanner = process[5]
        self.requisicao_modem = process[6]
        self.numero_disco = process[7]
        self.offset = None
        self.PID = None
        self.execucoes = 0

class GerenteProcessos:
    fila_prontos = [] #Engloba fila_tempo_real e fila_usuario
    fila_tempo_real = [] #Prioridade zero
    fila_usuario = [] #engloba prioridade 1, 2 & 3
    prioridade_1 = []
    prioridade_2 = []
    prioridade_3 = []
    em_execucao = {}
    ultimoPID = 0