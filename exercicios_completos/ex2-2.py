import sys 
import re 

# neste programa apenas contamos o numero de ocorrencias da palavra "".


def search(word):
	with open("dicionario_medico.txt", "r") as f:
		content = f.readlines()
		ocorrencia = 0
		linhas = []

	for i, line in enumerate(content):
		matches = findall(word ,line)

		if matches:
			ocorrencia += len(matches)
			linhas.append(line)

	
print("Numero total de ocorrencias da palavra" + word + ": " + ocorrencia)




