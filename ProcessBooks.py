import nltk
import sys
from nltk.corpus import brown



sub={"SB":[""]} # empty dictionary
adj={"AJ":[""]}
both= {"b":[""]}
subtuples= {"SB":[("","")]}
x=0
for i in brown.tagged_words(): #each word is in a tuple with its descriptor
	if (i[1] == "NN" ):
		#sub["SB"].append(str(i[0])) #list of words 
		subtuples["SB"].append((str(i[0]), "SB")) #list of tuples
	if (i[1] == "JJ" ):
		adj["AJ"].append(str(i[0]))
	x+=1;


def to_file(key):
    with open("subtags.txt", "w") as f:
        f.write("[")
        for i in key:
            out = str(i)
            f.write(out + ", ")
        f.write("]")

#to_file(subtuples["SB"])
	
#there are 152470 words with the tag NN returned by brown.tagged_words
#print("Num words: ", x); 	
# things that are secondary substances (ie, species)
#if something is known to be a quality its an adjectives= 
#red is a noun
#capita -color -clothes -fur -skin
#basically 

#bool isColor(str i):
    
    