import nltk
from pickle import load
input = open('unitag.pkl', 'rb')
unigram_tagger = load(input) ##loading in the unigram tagger made in CombiningCorpora.py
input.close()
qual = open("qualitytest.txt", "w")
sub = open("substancetest.txt", "w")
act = open("actiontest.txt", "w")

# with open("allWords.txt", "w") as f:
# 	for i in words:
# 		tagged_word = unigram_tagger.tag([i])[0]
# 		if(tagged_word[1] == 'JJ'):
# 			f.write(tagged_word[0] + " ")

def sort_words(text_file):
	with open(text_file, "r") as f: 
		for line in f:
			for word in line.split():
				tagged_word = unigram_tagger.tag([word])[0]
	
				if 'JJ' == tagged_word[1]:
					qual.write(tagged_word[0]+ " ")
				if 'NN' == tagged_word[1]: 
					sub.write(tagged_word[0]+ " ")
				if 'VB' == tagged_word[1]:
					act.write(tagged_word[0]+ " ")

sort_words("allWords.txt")			

		
