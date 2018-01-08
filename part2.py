from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


example_sentence="This is an example showing off stop word filtration, and so on. "
stop_words=set(stopwords.words("english"))

#print(stop_words)

words=word_tokenize(example_sentence)
print(words)

##filtered_sentence=[]
##
##for item in words:
##        if item not in stop_words:
##            filtered_sentence.append(item)
##
##
##print(filtered_sentence)

            
filtered_sentence = [w for w in words if not w in stop_words]
