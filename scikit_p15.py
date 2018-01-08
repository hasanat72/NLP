import nltk
from nltk.tokenize import word_tokenize
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB

from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC
import pickle


documents=[(list(movie_reviews.words(fileid)),category)
          for category in movie_reviews.categories()
          for fileid in movie_reviews.fileids(category)]


random.shuffle(documents)

all_words=[]
for w in movie_reviews.words():
        all_words.append(w.lower())
        
#freqdist is ordered from most common to least common
#and word_features means words upto 3000 most common words
all_words=nltk.FreqDist(all_words)
word_features=list(all_words.keys())[:3000]

def find_features(document):
        words=set(document)
        features={}
        for w in word_features:
                features[w]=(w in words)
                
        return features

#print(find_features(movie_reviews.words('pos/cv000_29590.txt')))
featuresets=[(find_features(rev),category) for (rev,category) in documents]

training_set=featuresets[:1900]
testing_set=featuresets[1900:]

##classifier=nltk.NaiveBayesClassifier.train(training_set)
classifier_f=open("naivebyas.pickle","rb")
classifier=pickle.load(classifier_f)
classifier_f.close()



print("Original Naive Bayes Algo Accuracy: ", (nltk.classify.accuracy(classifier,testing_set))*100)
classifier.show_most_informative_features(15)

##MNB_classifier:

MNB_classifier=SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier Accuracy: ", (nltk.classify.accuracy(MNB_classifier,testing_set))*100)

###GaussianNB
##Gaussian_classifier=SklearnClassifier(GaussianNB())
##Gaussian_classifier.train(training_set)
##print("Gaussian_classifier Accuracy: ", (nltk.classify.accuracy(Gaussian_classifier,testing_set))*100)

#BernoulliNB
Bernoulli_classifier=SklearnClassifier(BernoulliNB())
Bernoulli_classifier.train(training_set)
print("Bernoulli_classifier Accuracy: ", (nltk.classify.accuracy(Bernoulli_classifier,testing_set))*100)


## LogisticRegression,SGDClassifier
## SVC,LinearSVC,NuSVC


#LogisticRegression
LogisticRegression_classifier=SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier Accuracy: ", (nltk.classify.accuracy(LogisticRegression_classifier,testing_set))*100)


#SGDClassifier
SGDClassifier_classifier=SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier Accuracy: ", (nltk.classify.accuracy(SGDClassifier_classifier,testing_set))*100)

#SVC
SVC_classifier=SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier Accuracy: ", (nltk.classify.accuracy(SVC_classifier,testing_set))*100)

#LinearSVC
LinearSVC_classifier=SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier Accuracy: ", (nltk.classify.accuracy(LinearSVC_classifier,testing_set))*100)



#NuSVC
NuSVC_classifier=SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier Accuracy: ", (nltk.classify.accuracy(NuSVC_classifier,testing_set))*100)
















