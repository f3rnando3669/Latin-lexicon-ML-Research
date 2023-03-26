# shows outpout of np_vp_processing.py
import pickle
with open('spaCY\proposition_list.pkl', 'rb') as f: #this method of creating a list of propositions and storing it as a pkl helps save time
	cur_prop_list = pickle.load(f)
	f.close()
with open('spaCY\subj_substance_list.pkl', 'rb') as f: #this method of creating a list of propositions and storing it as a pkl helps save time
	cur_subj_list = pickle.load(f)
	f.close()


for i in cur_prop_list:
    print(i)
    
# for i in cur_subj_list:
#     print(i)