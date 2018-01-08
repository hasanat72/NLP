import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
import os



os.chdir('C:\\Python')
stored_data=open("pos_token_chink.txt","w")
file=open("pos_data.txt")
raw=file.read()
tokenized=word_tokenize(raw)
def process_content():
    try:
        for i in tokenized[5:]:
            tagged=nltk.pos_tag(tokenized)
            nameEnt=nltk.ne_chunk(tagged)
            nameEnt.draw()
            
            
    except Exception as e:
        print(str(e))
process_content()




