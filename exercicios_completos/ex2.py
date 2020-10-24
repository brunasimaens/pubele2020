# criar um programa que recebe uma palavra como argumento e:
# conta o numero de ocorrencias da palavra no ficheiro gerado
# retorna as linhas onde estão as palavras 

import sys 
import re 
# dá acesso a substituição, findall, search



def procura(palavra):
	with open("dicionario_medico.txt", "r") as f:

		content = f.readlines()
#obtemos uma lista de todas as linhas do ficheiro
		num_ocorrencias = 0
		linhas = []

		for i, line in enumerate(content):
			matches = findall(rf"(?i:\b{palavra}\b)",line) 
			#lista com todas as ocorrências da palavra na linha

			line = line.rstrip()
			line = sub(rf"(?i:\b({palavra})\b)",r"<b>\1</b>",line)

			if matches:
				num_ocorrencias += len(matches)
				linhas.append(line) #guarda a linha

		for l in linhas:
			print(f"<p>{l}</p>\n")	
	print("Numero total de ocorrencias da palavra" + palavra + ": " + num_ocorrencias)



def main():
	palavra = sys.argv[-1]
	procura(palavra)

main()