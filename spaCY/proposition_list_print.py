# shows outpout of np_vp_processing.py
import pickle
import spacy
import explacy
nlp = spacy.load("en_core_web_sm")
with open('spaCY\proposition_list.pkl', 'rb') as f: #this method of creating a list of propositions and storing it as a pkl helps save time
	cur_prop_list = pickle.load(f)
	f.close()
with open('spaCY\subj_substance_list.pkl', 'rb') as f: #this method of creating a list of propositions and storing it as a pkl helps save time
	cur_subj_list = pickle.load(f)
	f.close()


explacy.print_parse_info(nlp, str(cur_prop_list[0][2]))
    
# for i in cur_subj_list:
#     print(i)