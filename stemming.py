from nltk.corpus import stopwords
from nltk.text import Text
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import os


os.chdir('c:\\python')
file=open('concordance.txt')
data=file.read()

stop_words=set(stopwords.words("english"))
##word=word_tokenize(data)
sample_sent="Hellow Ali, How you doing Ali, Ali Came here"
word=word_tokenize(sample_sent)
cc=Text(word)
cc.concordance('ali')
##for w in stop_words:
##        if w not in word:
##                print(w)
