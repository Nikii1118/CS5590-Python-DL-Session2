from bs4 import BeautifulSoup
import requests
import nltk.data
from nltk.tokenize import sent_tokenize,word_tokenize

#nltk.download()

url = "https://en.wikipedia.org/wiki/Google"
source=requests.get(url)
plain = source.text
soup = BeautifulSoup(plain, "html.parser")

file2 = open('input'+ '.txt','a+',encoding='utf-8')
body = soup.find('div', {'class': 'mw-parser-output'})
file2.write(str(body.text))

with open('input.txt','r',encoding="utf8") as inputData:
    TextData=inputData.read().replace('\n','')

'''with open('input.txt',encoding='utf8') as data:
    text= data.read().strip()'''

tokens=word_tokenize(TextData)
pos=nltk.pos_tag(tokens)
print(tokens[1:10])
print(pos[1:10])
from nltk.stem import PorterStemmer
ps=PorterStemmer()
for w in tokens:
    print(w,":",ps.stem(w))



from nltk.stem import WordNetLemmatizer
lem=WordNetLemmatizer()
for m in tokens:
    print(m,":",lem.lemmatize(m))

from nltk import ngrams
trigram=ngrams(TextData.split(),3)
for gram in trigram:
    print(gram)
print(str(trigram))

from nltk import wordpunct_tokenize,pos_tag,ne_chunk
print(ne_chunk(pos_tag(wordpunct_tokenize(TextData))))

