import nltk
from nltk.corpus import brown

##example taken from the NLTK Book
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
## _________________________________

sentence= "I want the one that is red"
sentence2= "the dog was red"
print(unigram_tagger.tag(sentence.split()))
print(unigram_tagger.tag(sentence2.split()))
# with the example unigram tagger, both "red" nouns get tagged as adjectives
sentence3 = " I still want to go to the park"
sentence4 = "the still water reflected the tops of the trees"
print(unigram_tagger.tag(sentence3.split()))
print(unigram_tagger.tag(sentence4.split()))
# "still" gets tagged as an adverb in both cases here. 

