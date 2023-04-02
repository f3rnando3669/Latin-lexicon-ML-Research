import pickle
import sys

def tofile(pkl, newfile):
	with open(pkl, 'rb') as fl: 
		lst = pickle.load(fl)
		fl.close()
	with open(newfile, 'w') as f:
		for i in lst:
			f.write(str(i) + "\n")
		f.close()

tofile('spaCY\proposition_list.pkl', 'spaCY\cur_prop_txt.txt')
# tofile('spaCY\subj_substance_list.pkl', 'spaCY\cur_subj_txt.txt')
# tofile('spaCY\subj_vb_obj.pkl', 'spaCY\cur_svo_txt.txt')
# tofile('spaCY\quant_list.pkl', 'spaCY\cur_quant_txt.txt')