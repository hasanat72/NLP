from nltk.corpus import wordnet
syns=wordnet.synsets("good")

print(syns)
print(syns[0].lemmas())
print(syns[0].lemmas()[0].name())
print(syns[3].lemmas())
