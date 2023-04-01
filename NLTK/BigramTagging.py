import nltk
from nltk.corpus import brown
from nltk.corpus import treebank

size = int(len(brown.tagged_sents()))

training_data = brown.tagged_sents()[500:size] #giving it a lower amt of training data

backing_gram = nltk.UnigramTagger(training_data)

bigram_tagger = nltk.BigramTagger(training_data, backoff=backing_gram) # essentially, any word that the bigram doesn't know 
#will be pushed onto the unigram tagger
#_______________________________________________________________
# confusion_matrix = bigram_tagger.confusion(training_data[20:30]) 

# print(confusion_matrix) 


testing_data = brown.tagged_sents()[0:200]
testing_data2 = treebank.tagged_sents()[40:60]

acc = bigram_tagger.accuracy(testing_data)

acc2 = bigram_tagger.accuracy(testing_data2)

print("This is the accuracy of the bigram_tagger with data from the brown corpus", acc)
print("This is the accuracy of the bigram_tagger with data from the treebank corpus", acc2)

#the bigram tagger still had a low degree of accuracy when given a completely different corpus, but it had 
#a slightly higher degree of accuracy than the unigram tagger by itself.

# Saving Bigram tagger to use in other places without having to train it every time
# from pickle import dump
# output = open('btag.pkl', 'wb')
# dump(bigram_tagger, output, -1)
# output.close()