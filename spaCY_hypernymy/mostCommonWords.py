import spacy
from nltk.corpus import brown
import pickle

sents = brown.sents(categories = "learned") #there are 98,552 sentences in the gutenberg nltk corpus 

nlp = spacy.load("en_core_web_sm") # loading in language model

num_to_nouns = {"": 0}

def to_pkl(list, file):
    with open(file, 'wb') as f:
        pickle.dump(list, f)
        f.close()
        
def valid_noun(i):
    return (i.tag_ == "NN" or i.tag_ == "NNS") and i.tag_ != "WP" and i.lower_!="this" and i.lower_!="that"  and i.lower_!="these" and  i.lower_!="those" and i.lower_!="which" and len(i.lower_) > 2

def to_dictionary(list, dict):
	for x in list:
		sent= " ".join(x)
		doc= nlp(sent)
		for i in doc: 
			if valid_noun(i):
				i = i.lemma_
				if i in dict.keys():
					dict[i] = dict[i]+1 
				else:
					dict.update({i : 1})

# to_dictionary(sents, num_to_nouns)

# to_pkl(num_to_nouns, "spaCY_hypernymy/num_to_nouns.pkl")

with open("spaCY_hypernymy/num_to_nouns.pkl", 'rb') as fl: 
	num_to_nouns = pickle.load(fl)
	fl.close()

num_to_nouns.pop("")
# for i in num_to_nouns:
# 	if num_to_nouns.get(i) > 65:
# 		print(i, " ", str(num_to_nouns.get(i)))

def make_sortable_list(dict):
    sort_list = []
    for i in dict.keys():
        sort_list.append((i, dict[i]))
       
    return sort_list;


def notsorted(itemlist):
    for i in range (len(itemlist)-1):
        i_obj = itemlist[i]
        for j in range ((i+1), (len(itemlist))): 
            j_obj = itemlist[j]
            return i_obj[1] < j_obj[1]

def numer_order(item_list): #uses bubble sort
	ret_dict= {}
	while notsorted(item_list):
		for i in range (len(item_list)):
			for j in range ((i+1), (len(item_list)-1)):
				if item_list[i][1] < item_list[j][1]:
					item_list[j], item_list[i] = item_list[i], item_list[j] 
     
	for i in item_list:
		if len(ret_dict) < 100:
			ret_dict.update({i[0]: i[1]})
  
	return ret_dict
        
sortable_list = make_sortable_list(num_to_nouns)
num_to_nouns = numer_order(sortable_list)


to_pkl(num_to_nouns, "spaCY_hypernymy/100_most_common.pkl")
# for i in num_to_nouns: 
#     print(i + " " + str(num_to_nouns[i]))


# print(len(num_to_nouns.keys()))