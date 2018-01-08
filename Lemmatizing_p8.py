from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string
lemmatizer=WordNetLemmatizer()

##print(lemmatizer.lemmatize("cats"))
##print(lemmatizer.lemmatize("dogs"))
##print(lemmatizer.lemmatize("geese"))
##print(lemmatizer.lemmatize("best"))
##print(lemmatizer.lemmatize("females"))
##print(lemmatizer.lemmatize("better",pos="a"))
##
##print(lemmatizer.lemmatize("running",'v'))

sample_sentence="Hellow, How you doing, successfully you passed the exam... "
tokenized=word_tokenize(sample_sentence)
for item in tokenized:
        print(lemmatizer.lemmatize(item,pos="v"))


