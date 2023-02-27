import nltk
from pickle import load
input = open('btag.pkl', 'rb')
bigram_tagger = load(input)
input.close()

#checking to see that this loaded in bigram tagger works ___________________
example_sentence = "I want to go on a walk".split()
tag_sent = bigram_tagger.tag(example_sentence)
#print(tag_sent)
#___________________________________________________________________________

def proc_file(file, tagger):
	with open(file) as f:
		for line in f:
			for word in line.split():
				x = tagger.tag([word])[0]
				if(x[1] != 'JJ'):
					print(x)

#proc_file("filteredprobwords.txt", bigram_tagger)
#proc file returns: 
# #('right', 'QL') // qualifier (like very, fairly)
# ('general', 'JJ-HL')   // adjective word appearing in a headline
# ('individual', 'JJ-HL') // adjective word appearing in a headline
# ('formative', 'NN') // seems to be a noun when it comes to describing something in linguistics, a formative
