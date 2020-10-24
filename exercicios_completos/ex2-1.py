import sys 
import re 

# neste programa apenas contamos o numero de ocorrencias da palavra "".


with open("dicionario_medico.txt", "r") as f:
	content = f.read()
	ocorrencia = content.count("parto")

print("Numero total de ocorrencias da palavra: "+ str(ocorrencia))