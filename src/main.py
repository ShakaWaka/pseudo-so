import modulo_mem as mm
import modulo_es as mes
import modulo_arq as ma
import modulo_proc as mp
import sys


def main ():

	gerenteProcessos = mp.GerenteProcessos()

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


if __name__ == '__main__':
    main()
