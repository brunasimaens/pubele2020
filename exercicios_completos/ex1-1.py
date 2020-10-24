from re import *
import sys 


with open("dicionario_medico.txt", "r") as f:
	newfile = f.read()

newfile = newfile.replace ('^L', '\n')	

with open("dicionario_medico1.txt", "w") as f:
	f.write(newfile)

## neste programa, abrimos o ficheiro dicionario_medico.txt, lemos o ficheiro, 
## fizemos o replacement de ^L por \n
## de seguida criamos outro ficheiro dicionario_medico1.txt com essa mudança 