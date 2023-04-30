import spacy
from nltk.corpus import brown
import pickle

sents = brown.sents(categories = "learned") #there are 98,552 sentences in the gutenberg nltk corpus 

nlp = spacy.load("en_core_web_sm") # loading in language model

np_list_learned = []

be_sents = [];
ap_lem_sents = [];

def lemmatize(sent): 
    doc = nlp(sent)
    out = []
    for token in doc:
        out.append(token.lemma_)
    return " ".join(out)

def get_one_word_VP(list):
	output=[]
	vp = ""
	nsubj = "" 
	for x in list:
		sent= " ".join(x)
		doc= nlp(sent)
		for chunk in doc.noun_chunks:
			if chunk.root.dep_ == "nsubj" and chunk.root.tag_ != "NNP" and chunk.root.tag_ != "NNPS" and chunk.root.tag_ != "PRP" and chunk.root.tag_ != "WP" and chunk.root.lower_!="this" and chunk.root.lower_!="that"  and chunk.root.lower_!="these" and  chunk.root.lower_!="those" and chunk.root.lower_!="which" and len(chunk.root.lower_) > 2:
				vp = "" 
				np_vp = ["", ""]
				nsubj = chunk.root
				for child in nsubj.head.rights:
					for ch in child.subtree: 
						if ch.dep_ == "nsubj":
							break
						vp = vp +" "+str(ch)
				vp = str(nsubj.head) + vp
				vp = nlp(vp)
				for token in vp: 
					if token.dep_ == "ROOT" and len(vp) == 1:
						np_vp[0] = str(chunk)
						np_vp[1] = vp
						if np_vp[0] != "":
							output.append(np_vp)
						break
	return output

def get_hyp_base(list,sentlist):
    
	output=[]
	vp = ""
	nsubj = "" 
	for x in list:
		sent= " ".join(x)
		doc= nlp(sent)
		for chunk in doc.noun_chunks:
			if chunk.root.dep_ == "nsubj" and chunk.root.tag_ != "NNP" and chunk.root.tag_ != "NNPS" and chunk.root.tag_ != "PRP" and chunk.root.tag_ != "WP" and chunk.root.lower_!="this" and chunk.root.lower_!="that"  and chunk.root.lower_!="these" and  chunk.root.lower_!="those" and chunk.root.lower_!="which" and len(chunk.root.lower_) > 2:
				vp = "" 
				np_vp = ["", ""]
				nsubj = chunk.root
				for child in nsubj.head.rights:
					for ch in child.subtree: 
						if ch.dep_ == "nsubj":
							break
						vp = vp +" "+str(ch)
				vp = str(nsubj.head) + vp
				vp = nlp(vp)
				for token in vp: 
					if token.dep_ == "ROOT" and (token.lemma_ == "be"): 
						np_vp[0] = str(chunk)
						np_vp[1] = vp
						if np_vp[0] != "":
							output.append(np_vp)
							np_list_learned.append(str(nsubj))
						sentlist.append(lemmatize(sent))
						break
	return output


def get_AP_VP(list,sentlist):
    
	output=[]
	vp = ""
	nsubj = "" 
	for x in list:
		sent= " ".join(x)
		doc= nlp(sent)
		for chunk in doc.noun_chunks:
			if chunk.root.dep_ == "nsubj" and chunk.root.tag_ != "NNP" and chunk.root.tag_ != "NNPS" and chunk.root.tag_ != "PRP" and chunk.root.tag_ != "WP" and chunk.root.lower_!="this" and chunk.root.lower_!="that"  and chunk.root.lower_!="these" and  chunk.root.lower_!="those" and chunk.root.lower_!="which" and len(chunk.root.lower_) > 2:
				vp = "" 
				ap = ""
				ap_vp = ["", ""]
				nsubj = chunk.root
				for child in nsubj.head.rights:
					for ch in child.subtree: 
						if ch.dep_ == "nsubj":
							break
						vp = vp +" "+str(ch)
				vp = str(nsubj.head) + vp
				vp = nlp(vp)
				for child in nsubj.head.lefts:
					for ch in child.subtree: 
						if ch.dep_ == "amod":
							ap = ap + " " + str(ch)
				for token in vp: 
					if token.dep_ == "ROOT" and (token.lemma_ == "be"): 
						ap_vp[0] = ap
						ap_vp[1] = vp
						if ap_vp[0] != "":
							output.append(ap_vp)
							np_list_learned.append(str(nsubj))
						sentlist.append(lemmatize(sent))
						break
	return output




# out = get_hyp_base(sents,be_sents)
# ap_out = get_AP_VP(sents, ap_lem_sents)
# one_vp = get_one_word_VP(sents)
# out = out + ap_out
# be_sents = be_sents + ap_lem_sents


# def to_pkl(list, file):
#     with open(file, 'wb') as f:
#         pickle.dump(list, f)
#         f.close()

# to_pkl(one_vp, 'spaCY_hypernymy\_all_oneVP_pairs.pkl')
# to_pkl(out, 'spaCY_hypernymy\_all_pairs.pkl')
# to_pkl(be_sents, 'spaCY_hypernymy\get_all_lemma_sents.pkl')

    