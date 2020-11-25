from re import *
import jinja2 as j2
from bs4 import BeautifulSoup

infile = open("reports.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')

reports = soup.find_all('report')
a = reports

def extract_dict(l,a):
	info = {}
	for elem in l:
		v=search(rf"<{elem}>((?:.|\n)*?)</{elem}>",a)
		if v:
			info[elem]=v[1]
	return info

def extrai_listaH(xml,tag):
	info = []
	for miolo in findall(rf'<{tag}>((?:.|\n)*?)</{tag}>',xml):
		info.append(miolo)

	return info


def extrai_report1():
	l_dic = []
	t = j2.Template( """
<html>
<head>
  <title> Portfolio </title>
  <meta charset="UTF-8"/>
 <style>
body {background-color:rgba(156, 106, 27, 0.2);}
h1   {
	color: black;
	font-family: georgia;
	font-size: 250%
	}
p   {
	color: black;
	font-family: georgia;
	font-size: 150%
	}
h2   {
	color: black;
	font-family: georgia;
	font-size: 220%
	}
ol   {
	color: black;
	font-family: georgia;
	font-size: 150%
	}
</style>
</head>
<body>
 <h1 style="text-align:center"> {{title}} </h1>
 <p style="text-align:center"> {{date}} </p>
 <h2>Autores</h2>
 <ol>
    {% for el in team  %}
      <li> {{el['name']}} : {{el['email']}} </li>
    {% endfor %}
 </ol>
 <h2> Descrição </h2>
 <p> {{description}} </p>


</body>
</html>
""")
#preenche o template
	for i in range(len(a)):
		h = str(a[i])
		dic = extract_dict(['title','team','date','description' ],h)
		aux = extrai_listaH(dic['team'],'element')
		dic['team'] = [extract_dict(['name','email'],el) for el in aux]
		l_dic.append(dic)
#cria um link html para cada report criado
	for i in range(len(a)):
		#print(t.render(l_dic[i]))
		with open('report%s.html' % i, 'w') as file:
			file.write(t.render(l_dic[i]))

def main():
	extrai_report1()
main()

from bs4 import BeautifulSoup
xml_doc=open("reports.xml")

#buscar os titulos do relatório
L=[]
soup = BeautifulSoup(xml_doc, 'html.parser')
L=soup.find_all('title')
for el in range(len(L)):
    L[el]=L[el].text.strip()

part1=open("parte1.txt")
parte1=part1.read()
part3=open("parte3.txt")
parte3=part3.read()


def relat_part(L):
    text=''
    for i in range(len(L)):

    	text+="""  <a href= "report{nt}.html">{rt}</a><br>\n  """.format(nt=i, rt=L[i])
    text+="""  <a href="/Users/brunasimaens/desktop/informatica/PE/aulas/trabalhos/trabalhopratico1/xml2html.py">Codigo Python Utilizado</a>\n"""

    return(text)

# cria um índice com todos os ficheiros html
def cria_indice(L, parte1, parte3):
    middle=relat_part(L)

    ficheiro=open("index.html", "w")
    textofinal=parte1+middle+parte3
    ficheiro.write(textofinal)
    ficheiro.close()






cria_indice(L, parte1, parte3)
