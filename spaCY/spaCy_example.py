import nltk
import spacy
from nltk.corpus import brown
from spacy import displacy  #I was trying to work with d
import explacy ## found explacy in a link in the webpage that you sent over email 

nlp = spacy.load("en_core_web_sm") # loading in language model

dc = ""
sentences = brown.sents()[0:200]


# this function goes through x, which is treated as an iterable of string lists (sentences), 
# and prints the dependency of each "token" in those sentences
def print_dependencies(x): 
	for sent in sentences: 
		dc = " ".join(sent)
		doc = nlp(dc)
		for token in doc:
			print(token, token.dep_, "\n")
   
# this function goes through x, (see above), and prints the dependencies of each of the 
# noun chunks found(the grammatical role of the current phrase)
options = {"compact": True, "bg": "#09a3d5",
           "color": "white", "font": "Source Sans Pro"}

def print_depen_phrase(x): 
	for sent in x: 
		dc = " ".join(sent)
		doc = nlp(dc)
		for chunk in doc.noun_chunks:
			print(chunk, chunk.root.dep_, "\n")

def print_all_dependency(x):
	for sent in x: 
		dc = " ".join(sent)
		explacy.print_parse_info(nlp, dc)

# print_dependencies(sentences)
# print_depen_phrase(sentences)
# print_dependencies(sentences)

sent = "The wind was blowing fiercely over the trees"
explacy.print_parse_info(nlp, sent)