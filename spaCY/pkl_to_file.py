import pickle
import sys

with open('spaCY\proposition_list.pkl', 'rb') as f: #this method of creating a list of propositions and storing it as a pkl helps save time
	cur_prop_list = pickle.load(f)
	f.close()
with open('spaCY\subj_substance_list.pkl', 'rb') as f: #this method of creating a list of propositions and storing it as a pkl helps save time
	cur_subj_list = pickle.load(f)
	f.close()
with open('spaCY\subj_vb_obj.pkl', 'rb') as f:
    cur_svo_list= pickle.load(f)
    f.close()
    
    
def tofile(list, newfile):
	with open(newfile, 'w') as f:
		for i in list:
			f.write(str(i) + "\n")
		f.close()

tofile(cur_prop_list, 'spaCY\cur_prop_txt.txt')
tofile(cur_subj_list, 'spaCY\cur_subj_txt.txt')
tofile(cur_svo_list, 'spaCY\cur_svo_txt.txt')