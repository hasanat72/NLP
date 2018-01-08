from nltk.corpus import wordnet
syns=wordnet.synsets("plan")
##print(syns)
##print(syns[3].name())
##print(syns[1].lemmas()[0].name())
##
##
###definition for specific word
##
##print(syns[0].definition())
##
###example
##
##print(syns[0].examples())



##synonyms=[]
##antonyms=[]
##d=(wordnet.synsets("good"))
##print(d)
##print(d[3].lemmas())
##
##for syn in wordnet.synsets("good"):
##        for l in syn.lemmas():
####            print ("l:",l)
####            print(l.name())
##            synonyms.append(l.name())
##            if l.antonyms():
##                antonyms.append(l.antonyms()[0].name())
##                
##print(set(synonyms))
##print(set(antonyms))



#similarity--ship.nounn.first set

w1=wordnet.synset("bike.n.01")
w2=wordnet.synset("cactus.n.01")
print(w1.wup_similarity(w2))
































