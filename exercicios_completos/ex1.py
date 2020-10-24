# descarregar o ficheiro dicionario_medico.txt
# ex 1 - criar um programa que gera um novo ficheiro, substituindo todas as ocorrencias do caracter '\x0c' (ou ^L) por um '\n'.

#ler o ficheiro dicionario_medico

with open("dicionario_medico.txt", "r") as f:
# abrir canal para ler dicionario
	content = f.read()
## content tem todas as linhas, lemos dicionario em variavel content

	res = content.replace ('\f', '\n') # new content
	print (content)

