class Arquivo:
    def __init__(self, arquivo, criador=None):
        self.nome = arquivo[0]
        self.bloco_inicio = int(arquivo[1])
        self.tamanho = int(arquivo[2])
        self.criador = criador

class OperacaoArquivo:
    def __init__(self, operacao):
        self.PID = int(operacao[0])
        self.opcode = int(operacao[1])
        self.arquivo = operacao[2]
        if(self.opcode == 0):
            self.tamanho = int(operacao[3])
        else:
            self.tamanho = None

class GerenteArquivos:
    qtd_blocos = 0
    qtd_segmentos = 0
    arquivos = []
    operacoes = []
    #Lista de blocos do disco
    disco = []
    #Saidas do gerenciador de arquivos
    log = []
    # os dados devem ficar residentes no disco
    def inicia_disco(self):
        self.disco = [0 for i in range(self.qtd_blocos)]
        for arq in self.arquivos:
            self.disco[arq['bloco_inicio']:arq['bloco_inicio'] + arq['tamanho']] = arq['tamanho']*[arq['nome']]
        #o algoritmo a ser usado no armazenamento do disco (embora nao seja usual ser usado na alocacao do disco) seja o first-fit 

