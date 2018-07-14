import urllib.request
from bs4 import BeautifulSoup

url = "https://economia.uol.com.br/noticias/reuters/2018/07/11/cmo-aprova-texto-base-da-ldo-2019.htm" #"https://economia.uol.com.br/noticias/reuters/2018/07/11/cmo-aprova-texto-base-da-ldo-2019.htm" "https://g1.globo.com/rj/rio-de-janeiro/noticia/delator-diz-que-nada-era-feito-no-governo-cabral-sem-o-consentimento-de-picciani.ghtml"
pageurlopen = urllib.request.urlopen(url) #Extrai o html do link
pagebs = BeautifulSoup(pageurlopen.read(), 'html.parser') #Passando html pela biblioteca BeautifulSoup4
html = pagebs.prettify() #Esta função formata o html, deixando a estrutura organizada e identada
#title = pagebs.title.string
#all_links = pagebs.find_all('a')
#all_div = pagebs.div.prettify()
h1 = ''

#Extrair tags que contém texto
for count in range(0, len(html)):
    if html[count:count+3] == '<h1' or html[count:count+3] == '<h2' or html[count:count+3] == '<p ' or html[count:count+3] == '<p>':
        aux = count
        while html[aux:aux+4] != '</h1' and html[aux:aux+4] != '</h2' and html[aux:aux+4] != '</p>':
            h1 = h1 + html[aux]
            aux = aux + 1
            count = aux
        if html[aux:aux + 3] == '</p':
            h1 = h1 + html[aux:aux+4]
        else:
            h1 = h1 + html[aux:aux + 5]

#Extrair texto do HTML
count2 = 0
extracttext = ''
while count2 < len(h1):
    if h1[count2] == '<':
        while h1[count2] != '>':
            count2 = count2 + 1
    elif h1[count2] == '>':
        count2 = count2 + 1
    else:
        while h1[count2] != '<':
            extracttext = extracttext + h1[count2]
            count2 = count2 + 1

#Remover excesso de quebra e espaços

fixtext = ''

for c in range(0, len(extracttext)):
    if extracttext[c-1] == '\n' and extracttext[c] != ' ':
        fixtext = fixtext + extracttext[c]
    elif (extracttext[c - 1] == ' ' or extracttext[c-1] == '\n') and (extracttext[c] == ' ' or extracttext[c] == '\n'):
        extracttext #não faço nada
    else:
        fixtext = fixtext + extracttext[c]

print(fixtext) 
