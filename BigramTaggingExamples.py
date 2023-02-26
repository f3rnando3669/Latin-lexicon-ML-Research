#this .py program just contains examples and testing of the bigram tagger from the nltk book 
# from UnigramTagging import myunigramtagger
import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
bigram_tagger = nltk.BigramTagger(brown_tagged_sents)

## _________________________________

sentence= "I want the one that is red"
sentence2= "the dog was red"
print(bigram_tagger.tag(sentence.split()))
print(bigram_tagger.tag(sentence2.split()))
# with the example unigram tagger, both "red" nouns get tagged as adjectives
#here, the bigram tagger is missing some parts, since it hasn't been trained on that data
sentence3 = " I still want to go to the park"
sentence4 = "the still water reflected the tops of the trees"
print(bigram_tagger.tag(sentence3.split()))
print(bigram_tagger.tag(sentence4.split()))
# "still" gets tagged as an adverb in both cases here with the unigrammer, but 
#with the bigram tagger, there's again missing parts. 
