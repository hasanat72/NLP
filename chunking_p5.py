import nltk
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize

sample_text=state_union.raw("2006-GWBush.txt")
#print(sample_text)
tokenized=sent_tokenize(sample_text)

for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            chunkGram="""Findings: {<RB.?>*<VB.?>*<NNP>*<NN>?}"""
            chunkParser=nltk.RegexpParser(chunkGram)
            chunked=chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()
