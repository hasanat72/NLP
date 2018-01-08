import nltk
##from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
train_text="Lovely Python doing well"
sample_text="Python Doing well"
custom_tokenizer = PunktSentenceTokenizer(train_text)
tokens=custom_tokenizer.tokenize(sample_text)

def pos_analysis():
    try:
        for word in tokens:
                words=nltk.word_tokenize(word)
                tagged=nltk.pos_tag(words)
                print(tagged)
                
    except Exception as e:
                print(str(e))

pos_analysis()
