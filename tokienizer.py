import nltk
#nltk.download()
from nltk.tokenize import sent_tokenize,word_tokenize
example_text="Hellow,Mr.Robin how are you? The sky is pinkish blue."
# tokenize by sentence

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for items in word_tokenize(example_text):
        print(items)

        
for items in sent_tokenize(example_text):
        print(items)
