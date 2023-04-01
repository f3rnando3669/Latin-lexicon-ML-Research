#In this file, I'll be trying to combine all the tagged sentences from the brown and treebank corpuses 
#and train my unigram tagger
import nltk
from nltk.corpus import brown
from nltk.corpus import treebank

brownCorp = brown.tagged_sents()
treebankCorp = treebank.tagged_sents()

# size = int(len(brownCorp)) #checked sizes to see that it actually combined
# size2 = int(len(treebankCorp))

combo = brownCorp.__add__(treebankCorp) # combo contains brown tagged sentences, treebank tagged sentences

size3 = int(len(combo))
# print(size, "\n", size2 ,"\n", size3)
training_set = combo[50:size3] # gave it a massive training set
testing_set = combo[0:50]

unigram_tagger= nltk.UnigramTagger(training_set)


# acc = unigram_tagger.accuracy(treebankCorp[0:50])
# print("This is the accuracy", acc)



# Saving unigram tagger to use in other places without having to train it every time
from pickle import dump
output = open('unitag.pkl', 'wb')
dump(unigram_tagger, output, -1)
output.close()