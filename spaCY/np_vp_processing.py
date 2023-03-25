import sys
import spacy
from nltk.corpus import brown
import explacy ## found explacy in a link in the webpage that you sent over email 
sents=brown.sents(categories='fiction') #there is about 4000 sentences in this 

nlp = spacy.load("en_core_web_sm") # loading in language model

# print(" ".join(sents[1]));

# given a list of lists of strings, separate out the np and vp, put in a new list of tuples of strings:
# [(NP1,VP1), (NP2,VP2), (NP3,VP3), ....]
def get_np_vp(list):
	output=[]
	nsubj = "" 
	for x in list: 
		sent= " ".join(x)
		print("\n", sent, "\n")
		doc= nlp(sent)
		for chunk in doc.noun_chunks:
			if chunk.root.dep_ == "nsubj":
				print("\n", chunk)
				nsubj = chunk.root
				print(nsubj.head, "\n")
				print([child for child in nsubj.head.lefts])
		#	if (token.dep_ == 'ROOT' or token.dep_ == 'aux') and (token.pos_ == "VERB" or token.pos_ == "AUX"):
		# 		print("\n", token, [child for child in token.children], "\n") # the children of the root node contain the words before the entire phrase as well
				# if token.dep_ == 'nsubj':

			

get_np_vp(sents[100:110])
    