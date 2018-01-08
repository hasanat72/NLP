import nltk
from nltk.tokenize import word_tokenize
import random
from nltk.corpus import movie_reviews


documents=[(list(movie_reviews.words(fileid)),category)
          for category in movie_reviews.categories()
          for fileid in movie_reviews.fileids(category)]


##documents=[]
##for category in movie_reviews.categories():
##        for fileid in movie_reviews.fileids(category):
##            documents.append(list(movie_reviews.words(fileid)))

random.shuffle(documents)

##print(documents[1])
all_words=[]
for w in movie_reviews.words():
        all_words.append(w.lower())
        
#freqdist is ordered from most common to least common
all_words=nltk.FreqDist(all_words)
print(all_words.keys())[:10]

##word_features=list(all_words.keys())[:30]
##
##
##def find_features(document):
##        words=set(document)
##        features={}
##        for w in word_features:
##                features[w]=(w in words)
##                
##        return features
##
##print(find_features(movie_reviews.words('pos/cv000_29590.txt')))
##featuresets=[(find_features(rev),category) for (rev,category) in documents]
