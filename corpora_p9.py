from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize




sample=gutenberg.raw("bible-kjv.txt")
tok=sent_tokenize(sample)


# prints sentences from 5 to 1 after tokenization 
for items in tok[5:15]:
        print(items)

