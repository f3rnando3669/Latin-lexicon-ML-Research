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
# with open('spaCY\subj_vb_obj.pkl', 'rb') as f:
#     cur_svo_list= pickle.load(f)
#     f.close()
    

# for i in cur_subj_list:
#     print(i)

# for i in cur_prop_list:
# 	print(i)

# for i in cur_svo_list: 
#     print(i)

# ####################################### this is what I did to get the subj_vb_obj pkl file
def sub_vb_obj(list):
	sub_vb_obj_lst = []
	for i in list: 
		vp = nlp(i[2])
		for token in vp: 
			if token.dep_ == "dobj":
				sub_vb_obj_lst.append([i[0], i[1], str(token)])
	return sub_vb_obj_lst

svo = sub_vb_obj(cur_prop_list)

with open('spaCY\subj_vb_obj.pkl', 'wb') as f:
    pickle.dump(svo, f)
    f.close()