import os
import nltk
import string
from nltk.tokenize import word_tokenize, sent_tokenize,RegexpTokenizer
from nltk.corpus import stopwords
##os.getcwd()
os.chdir('C:/python')

file= open('data2.txt')
raw=file.read()

stop_words=set(stopwords.words("english"))
for item in word_tokenize(raw):
    print (item)
    
for item in sent_tokenize(raw):
    print (item)

for punct in string.punctuation:
         raw=raw.replace(punct,"")

print("\n :D You see from now on there is no punctuation mark, all has been replaced by space")
print("\n")

print(raw)

#building a set of wrods with all english stop_words, that is predefined    
stop_words=set(stopwords.words("english"))  

filtered_data=[]
words=word_tokenize(raw)
for word in words:
        if word not in stop_words:
                filtered_data.append(word)
                
print(filtered_data)
