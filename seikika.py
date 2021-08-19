# coding: utf-8

import MeCab
import collections 
import numpy as np

m = MeCab.Tagger("-Ochasen")
text = "ひまわりの種が50個あります。6個ずつ植木鉢に植えます。全部植えるには植木鉢は何個要りますか。"

# word_to_id = {}
# id_to_word = {}
# for word in text:
#     if word not in word_to_id:
#         new_id = len(word_to_id)
#         word_to_id[word] = new_id
#         id_to_word[new_id] = word
 
# corpus = np.array([word_to_id[w] for w in words])
 
# print ('id_to_word \n', id_to_word)
# print ('word_to_id \n', word_to_id)
# print ('corpus \n',corpus)


node = m.parseToNode(text)
words=[]
figures=[]

i = 1

while node:
    hinshi = node.feature.split(",")[1]
    if hinshi in ["一般"]:
        origin = node.feature.split(",")[6]
        words.append((origin,i))

    if hinshi in ["数"]:
        origin = node.surface.split(",")[0]
        figures.append((origin,i))
    node = node.next
    
    i += 1



print(words)
print(figures)

# print(m.parse(text))