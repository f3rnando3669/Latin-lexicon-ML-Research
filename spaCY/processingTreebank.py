import sys
import spacy
from nltk.corpus import treebank
import explacy ## found explacy in a link in the webpage that you sent over email 

nlp = spacy.load("en_core_web_sm") # loading in language model
fl = open("spaCY\dependencies.txt", "w")
dc = ""
sentences = treebank.sents()[0:200]
#			root = str(chunk.root)
#			dep = str(chunk.root.dep_)

def important_dependencies(x, file): ##
	with file as f: 
		for sent in x:
			f.write("\n\n")
			dc = " ".join(sent)
			f.write(dc + "\n")
			doc = nlp(dc)
			for token in doc:
				tok_dep= str(token.dep_)
				tok_pos= str(token.pos_)
				if tok_dep == "nsubj":
					f.write(str(token) + " " + tok_dep + " ")
				elif tok_dep == "dirobj" or tok_dep == "pobj":
					f.write(str(token) + " " + tok_dep + " ")
				elif tok_dep == "attr" or tok_dep == "acomp":
					f.write(str(token) + " " + tok_dep + " ")

   
def print_all_dependency(x):
	for sent in x: 
		dc = " ".join(sent)
		explacy.print_parse_info(nlp, dc)

  
important_dependencies(sentences, fl)

print_all_dependency(sentences[25:50])