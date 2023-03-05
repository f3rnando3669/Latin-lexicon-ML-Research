import nltk
from pickle import load
input = open('unitag.pkl', 'rb')
unigram_tagger = load(input) ##loading in the unigram tagger made in CombiningCorpora.py
input.close()
qual = open("textfiles/qualitytest.txt", "w")
sub = open("textfiles/substancetest.txt", "w")
act = open("textfiles/actiontest.txt", "w")
quant = open("textfiles/quantitytest.txt", "w")
rel = open("textfiles/relationtest.txt", "w")
qual.close()
sub.close()
act.close()

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
	
				# if 'JJ' == tagged_word[1]:
				# 	qual.write(tagged_word[0]+ " ")
				# if 'NN' == tagged_word[1]: 
				# 	sub.write(tagged_word[0]+ " ")
				# if 'VB' == tagged_word[1]:
				# 	act.write(tagged_word[0]+ " ")
				if 'JJR' == tagged_word[1] or 'JJS' == tagged_word[1] or 'JJT' == tagged_word[1]: 
					rel.write(tagged_word[0]+ "\n")
     

def sort_nums(text_file):
	with open(text_file, "r") as f: 
		for line in f:
			for word in line.split():
				tagged_word = unigram_tagger.tag([word])[0]
				if 'CD' == tagged_word[1]:
					quant.write(tagged_word[0]+ "\n")
					
sort_words("textfiles/allWords.txt")
sort_nums("textfiles/allWords.txt")