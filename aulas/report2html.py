from re import *

info={
"title":"TPC1",
"date":"29/10/2020",
"team":"<li>Bruna Ramoa<br>80825<br>#brunamiguelsimaens@hotmail.com<br></li>",
"description":"primeiro trabalho de htmk"
}


def extraxt():
	with open("reportxml.xml") as f:
		report=f.read()
	info=[]   #dicionario vazio
	v=search(r'<title>(.*)</title>', report)     #search devolve um tipo de dados (none- se nao encontrar), ou array
	if v:
		info["title"] =v[1]
		#print(v[1])                             # 0 da tudo, 1 da primeiro grupo de parentises
	#else:
		#print("-")
	v=search(r'<title>(.*)</title>', report)
	if v:
		info["date"] =v[1]

def subst(file,d):
	with open("template.html", 'r') as f:
		template=f.read()
	for key,value in info.items():                       ## para todos os pares (key value) do dicionario
		template=sub(rf'#{key}',rf'{value}', template)   #substituir a key pelo valor que está no template
	return(template)


def main():
	#print(subst("template.html", info))
	extract
main()
