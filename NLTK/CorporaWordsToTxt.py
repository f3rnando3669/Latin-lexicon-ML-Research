import nltk
import sys
from nltk.corpus import brown
from nltk.corpus import treebank

#idea here is to read all the words in a given corpus's "tagged_words()" to a dictionary, which will automatically filter the  
#repeated words, and make the writing to a file less of a hassle.

 
word_dict= {"": 0}


def update_dict(b, t, dict):
    for i in b: 
        dict.update({str(i[0]): 0})
    for x in t:
        dict.update({str(x[0]): 0})
    return dict
        
word_dict = update_dict(brown.tagged_words(), treebank.tagged_words(), word_dict)
    
    
def to_file(keylist, file):
    with open(file, "w") as f:
        for i in keylist:
            out = str(i)
            f.write(out + " ")
#the keyset of word_dict now contains all the words that were tagged in the corpora 
to_file(word_dict.keys(), "textfiles/allWords.txt")
