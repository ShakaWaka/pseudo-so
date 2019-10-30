import mem_manager as mem
import io_manager as iom
import file_manager as fm
import proc_manager as pm
import sys

if len(sys.argv) > 2:
    procFile = sys.argv[1]
    arqFile = sys.argv[2]
else:
    procFile = 'processes.txt'
    arqFile = 'files.txt'
