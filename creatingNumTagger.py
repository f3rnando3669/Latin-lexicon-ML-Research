import nltk 
from nltk.corpus import brown
from nltk.corpus import treebank
numberfile = open("textfiles/numberfile.txt", "w+")
def is_numerical(x): #this is a ridiculous function
    
	if '1' in x or '2' in x or '3' in x or '4' in x or '5' in x or '6' in x or '7' in x or '8' in x or '9' in x:
		return True 
	elif 'one' == x or 'two' in x or 'three' in x or 'four' in x or 'five' in x or 'six' in x or 'seven' in x or 'eight' in x or 'nine' in x:
		return True
	elif 'ten' == x or 'eleven' in x or 'thirty' in x or 'twelve' in x or 'thirteen' in x or 'fifteen' in x or 'twenty' in x or 'forty' in x or 'fifty' in x:
		return True
	elif 'hundred' in x or 'thousand' in x or 'million' in x or 'billion' in x or 'trillion' in x:
		return True
	else:
		return False

bwords = brown.tagged_words()
twords= treebank.tagged_words()

def sort_numberwords(write_file):
	for pair in bwords: 
		if is_numerical(str(pair[0])): 
			write_file.write(pair[0] + "\n")
	for pair in twords:
		if is_numerical(str(pair[0])): 
			write_file.write(pair[0] + " \n")
   
sort_numberwords(numberfile)

#noticed issue, numerical words like 'one' or 'ten' are substrings of words that are not numerical 
#also 