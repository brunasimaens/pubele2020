cabecalho = ''' <?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE xdxf SYSTEM "https://raw.github.com/soshial/xdxf_makedict/master/format_standard/xdxf_strict.dtd">
<xdxf lang_from="POR" lang_to="POR" format="logical" revision="033">
    <meta_info>
        <title>Dicionario medico</title>
        <full_title>Webster's Unabridged Dictionary</full_title>
        <description>Webster's Unabridged Dictionary published 1913 by the Webster 
        Institute</description>
        <file_ver>001</file_ver>
    <lexicon>'''


    #€<ar>
    #       <k>entrada</k>
    #       <def>
    #           </def>
    #   <ar>

from re import *
import sys


def transforma_dicionario(dicionario):

    with open(dic) as f:    

        content = f.read()
        entradas = split(r"\n{2,}" ,content) # splits por linhas em branco, e linhas em branco ou mais 
        nova = pros(entrada)
        for entrada in entradas:
            print(f"<ar>{entrada}</ar>")


def pros(entrada):
    entrada = sub()
#substituir a primeira linha 



def main():
    print(cabecalho)
    transforma_dic(sys.argv[1])
    print("</lexicon>")
    print("</xdxf>")

main()


                    
                