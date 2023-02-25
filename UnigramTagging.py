import nltk
import sys
from nltk.corpus import brown
from nltk.corpus import treebank

size = int(len(brown.tagged_sents()))

training_data = brown.tagged_sents()[40:size]#training data is 3000 of the brown tagged sentences

testing_data = brown.tagged_sents()[0:39]
testing_data2 = treebank.tagged_sents()[40:60]

unigram_tagger= nltk.UnigramTagger(training_data)

##________________________________________
##this confusion matrix shows the concurrency of the predicted and actual values. The number where predicted and actual were the same are given in <> 
##weirdly, it throws an error when I try to use testing_data. But I'm guessing that this is because it sees a word that it doesn't recoginize. 
confusion_matrix = unigram_tagger.confusion(training_data[20:30]) 

#print(confusion_matrix) 
##_______________________________________
#accuracy of the current unigram tagger

acc = unigram_tagger.accuracy(testing_data)
acc2 = unigram_tagger.accuracy(testing_data2)

print("This is the accuracy with data from the brown corpus", acc)
print("This is the accuracy with data from the treebank corpus", acc2)

#a much lower degree of accuracy when given data from a completely different corpus. 

#testing on individual words_______________________________________________________
blue = unigram_tagger.tag(["blue"])
red = unigram_tagger.tag(["red"])
print(blue)
print(red)
#both colors return JJ, or adjective, as their tags
#__________________________________________________________________________________
#using my program in ProcessBooks, I sorted all the words associated with noun/substance into listOfWords.txt
#now I can read in those strings, split and tag them with the unigram tagger. 
#from there, I'll see which ones do not return NN as a tag


def from_file(file):
	store = []
	with open(file, "r") as f:
		for line in f:
			store.extend(line.split())	
	
	return store	

words = from_file("listOfWords.txt") #gets all the words from the file into a list of words/ 

# for i in words:
#     tagged_word = unigram_tagger.tag(i)
    
    
 
	



