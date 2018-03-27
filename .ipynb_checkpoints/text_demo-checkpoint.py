text = ['I love this dogs, but it is too expensive? What do you think?', 
        'Where are you from? Your accent is strange.']

print('*'*10)
print('Splitter')
from text_hier_split import text2sents, sent2words
a = sent2words(text)
sents = a.proceed()
print(sents)

from token_idx_map import token2idx

temp = token2idx(sents)
print(temp.proceed())

#print(temp.map_text_idx())

# a = text[0]
# from collections import Counter
# words = a.split()
# print(Counter(words).most_common(5))

# print('*'*20)
# print('sent2word')
# b = sent2words(sents[0])
# c = b.proceed()
# print(c)



# print('*'*10)
# print('Cleaner')
# from text_preprocess import text_preprocess
# a = text_preprocess(text)
# print(a.proceed())

# from text_vectorizer import text_vectorizer
# from sklearn.feature_extraction.text import CountVectorizer  
# print('*'*10)
# print('Vectorizer')
# a = text_vectorizer(text, vectorizer=CountVectorizer())
# vecs = a.proceed()
# print(vecs[0])


