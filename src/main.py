import modulo_mem as mm
import modulo_es as mes
import modulo_arq as ma
import modulo_proc as mp
import sys
import operator

def main ():

	gerenteProcessos = mp.GerenteProcessos()
	sistemaArq = ma.GerenteArquivos()

	if len(sys.argv) > 2:
	    procFile = sys.argv[1]
	    arqFile = sys.argv[2]
	else:
	    procFile = 'processes.txt'
	    arqFile = 'files.txt'

	#Abre arquivo de processos
	with open(procFile, 'r') as f:
		#cria um aray de processos, atribuindo a cada variavel do tipo o valor no arquivo
	    procs = [[int(x) for x in linha.split(',')] for linha in f]
	    processes = [mp.Process(x).__dict__ for x in procs]

    #Abre e le o arquivo do sistema de arquivos
	with open(arqFile, 'r') as f:
		temp = f.read().splitlines()
		sistemaArq.qtd_blocos = int(temp[0])
		sistemaArq.qtd_segmentos = int(temp[1])
		sistemaArq.arquivos = [ma.Arquivo(temp[i].replace(' ', '').split(',')).__dict__ for i in range(2, sistemaArq.qtd_segmentos+2)]
		sistemaArq.operacoes = [ma.OperacaoArquivo(temp[i].replace(' ', '').split(',')).__dict__ for i in range(sistemaArq.qtd_segmentos+2, len(temp))]

if __name__ == '__main__':
    main()
