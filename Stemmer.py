from nltk.stem import PorterStemmer
import os
from nltk.tokenize import word_tokenize
os.chdir('C:\\python')

##file=open("stemmer.txt","w")
##data="Stemming stemmer stemmed stemmingly"
##file.write(data)
##file.close()
raw=open('stemmer.txt')
d=raw.read()
words=word_tokenize(d)
ps=PorterStemmer()

for w in words:
        print(PorterStemmer().stem(w))

