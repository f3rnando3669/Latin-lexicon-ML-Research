import spacy
import pickle
nlp = spacy.load("en_core_web_sm") # loading in language model

all_pairs = []
most_common_words = []
output = []

#loading in the list of all pairs: 
with open('spaCY_hypernymy\_all_pairs.pkl', 'rb') as f: 
	all_pairs = pickle.load(f)
	f.close()
#loading list of most common words: 
with open('spaCY_hypernymy\\100_most_common.pkl', 'rb') as f: #100_most_common contains a dictionary with words and the number of appearances
	most_common_words = pickle.load(f)
	most_common_words = list(most_common_words.keys())
	f.close()
 
with open('spaCY_hypernymy\_all_oneVP_pairs.pkl', 'rb') as f: 
	pairs_one_vp = pickle.load(f)
	f.close()
#loading list of lemmatized words: 
 

def lemmatize(sent): 
    doc = nlp(sent)
    out = []
    for token in doc:
        out.append(token.lemma_)
    return " ".join(out)

#checking to see if both X AND Y contain common word
def contains_and_common_word(i):
    for word in most_common_words:
        return word in str(lemmatize(i[0])) and word in str(lemmatize(i[1]))

#checking to see if X OR Y contain common word
def contains_common_word(i):
    for word in most_common_words:
        return word in str(lemmatize(i[0])) or word in str(lemmatize(i[1])) 
        
#checking if lemmatized sentence contains common word: 

def contains_common_lem(i):
	for word in most_common_words:
		return word in str(i)

#filtering functions: 
def filter_and_com_words(p_vp): 
    filtered_list = []
    for i in p_vp: 
        if contains_and_common_word(i):
           filtered_list.append(i)
    return filtered_list

def filter_or_com_words(p_vp): 
    filtered_list = []
    for i in p_vp: 
        if contains_common_word(i):
           filtered_list.append(i)
    return filtered_list

def filter_lemmatized_list(lm):
    ret_list = [] 
    for i in lm:
        if contains_common_lem(i):
            ret_list.append(i)
    return ret_list
            

def to_pkl(list, file):
    with open(file, 'wb') as f:
        pickle.dump(list, f)
        f.close()
        
# output = filter_and_com_words(all_pairs)
# print(output)
# one_vp_filt = filter_and_com_words(pairs_one_vp)

# print(one_vp_filt)

# to_pkl(output, 'spaCY_hypernymy\_pairs_containing_and_common.pkl')
# to_pkl(one_vp_filt, 'spaCY_hypernymy\_NP-VPoneword.pkl' )