import sys
import spacy
from nltk.corpus import gutenberg
import pickle
import explacy ## found explacy in a link in the webpage that you sent over email 
sents=gutenberg.sents() #there are 98,552 sentences in the gutenberg nltk corpus 

nlp = spacy.load("en_core_web_sm") # loading in language model

np_list_gutenberg = []

# print(" ".join(sents[1]));

# given a list of lists of strings, separate out the np and vp, put in a new list of lists of strings:
# [[NP1,VP1], [NP2,VP2], [NP3,VP3], ....]
#process: look at the noun chunks in each sentence, if it is the subject, look at its head value (the verb it is connected to)
def get_np_vp(list):
	output=[]
	vp = ""
	nsubj = "" 
	for x in list:
		sent= " ".join(x)
		# print("\n", sent, "\n")
		doc= nlp(sent)
		for chunk in doc.noun_chunks:
			if chunk.root.dep_ == "nsubj":
				vp = "" 
				np_vp = ["", ""]
				# print("\n", chunk)
				nsubj = chunk.root
     
				# print([child for child in nsubj.head.lefts])
				# print(nsubj.head, "\n")
				for child in nsubj.head.rights:
					for ch in child.subtree: 
						vp = vp +" "+str(ch)
				vp = str(nsubj.head) + vp
				np_vp[0] = str(chunk)
				np_vp[1] = vp
				if np_vp[0] != "":
					output.append(np_vp)
					np_list_gutenberg.append(str(nsubj))
	return output
	# for item in output:
	# 	print(item)
		#	if (token.dep_== 'ROOT' or token.dep_ == 'aux') and (token.pos_ == "VERB" or token.pos_ == "AUX"):
		# 		print("\n", token, [child for child in token.children], "\n") # the children of the root node contain the words before the entire phrase as well
				# if token.dep_ == 'nsubj':

#takes a list of lists: looks at [1] for the verbs to determine if the 
def get_props(list): #need to store as: (N, is/has, predicate tree) 
	vp = ""
    
	prop_list = []
	for np_vp in list:
		vp = nlp(np_vp[1])
		for token in vp: 
			if token.dep_ == "ROOT" and (token.lemma_ == "be" or token.lemma_ == "have"): 
				prop_list.append([np_vp[0], str(token), vp])
				break
	return prop_list
		
					
np_vp_list_gutenberg = get_np_vp(sents[2000:5000])
proplist_gutenberg = get_props(np_vp_list_gutenberg)

with open('spaCY\propostion_list.pkl', 'wb') as f:
	pickle.dump(proplist_gutenberg, f)
	f.close()

with open ('spaCY\subj_substance_list.pkl', 'wb') as f:
	pickle.dump(np_list_gutenberg, f)
	f.close()