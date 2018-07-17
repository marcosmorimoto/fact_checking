import urllib.request
from bs4 import BeautifulSoup

url = "https://exame.abril.com.br/mundo/trump-comete-uma-tremenda-gafe-ao-se-encontrar-com-rainha-elizabeth-ii/" #"https://economia.uol.com.br/noticias/reuters/2018/07/11/cmo-aprova-texto-base-da-ldo-2019.htm" "https://g1.globo.com/rj/rio-de-janeiro/noticia/delator-diz-que-nada-era-feito-no-governo-cabral-sem-o-consentimento-de-picciani.ghtml"
pageurlopen = urllib.request.urlopen(url) #Extrai o html do link
pagebs = BeautifulSoup(pageurlopen.read(), 'html.parser') #Passando html pela biblioteca BeautifulSoup4

#remover tags desnecessárias
[s.extract() for s in pagebs('lable')]
[s.extract() for s in pagebs('input')]
[s.extract() for s in pagebs('br')]
[s.extract() for s in pagebs('em')]

html = pagebs.prettify() #Esta função formata o html, deixando a estrutura organizada e identada

texttags = ''

#Extrair tags que contém texto
for count in range(0, len(html)):
    if html[count:count+3] == '<h1' or html[count:count+3] == '<h2' or html[count:count+3] == '<p ' or html[count:count+3] == '<p>':
        aux = count
        while html[aux:aux+4] != '</h1' and html[aux:aux+4] != '</h2' and html[aux:aux+4] != '</p>':
            texttags = texttags + html[aux]
            aux = aux + 1
            count = aux

        if html[aux:aux + 3] == '</p':
            texttags = texttags + html[aux:aux+4]
        else:
            texttags = texttags + html[aux:aux + 5]

#Extair somente o texto das tags
text = BeautifulSoup(texttags, 'html.parser').text

#Remover excesso de quebra e espaços

fixtext = ''

for c in range(0, len(text)):
    if text[c-1] == '\n' and text[c] != ' ' and text[c] != '\n':
        fixtext = fixtext + text[c]
    elif (text[c - 1] == ' ' or text[c-1] == '\n' or text[c-1] == '\n ' or text[c - 1] == '') and (text[c] == ' ' or text[c] == '\n' or text[c] == '\n ' or text[c] == ''):
        text #não faço nada
    else:
        fixtext = fixtext + text[c]

#Separar texto por linhas

textlines = list()
lineaux = ''
line = 0

for c in range(0, len(fixtext)):
    if fixtext[c] != '\n':
        lineaux = lineaux + fixtext[c]
    else:
        textlines.append(lineaux)
        lineaux = ''
        line = line + 1

print(textlines)