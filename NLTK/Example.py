import nltk
from nltk import CFG, RecursiveDescentParser, TreePrettyPrinter
from nltk.tree import *
#experimenting with part-of-speech tagging 
oblv= (["My", "life" ,"is", "drab", "and",  "wretched",  "by", "comparison"])
o_tagged = str(nltk.pos_tag(oblv))

oblv_grammar = CFG.fromstring(
	""" S -> NP VP PP 
 		NP -> Det N
		PP -> P N
		P -> 'by'
		N -> 'life' | 'comparison'
		VP -> V ADJ CONJ ADJ
		V -> 'is' 
		ADJ -> 'drab' | 'wretched' 
		CONJ -> 'and' 
		Det -> 'My'
   		"""
)
print(oblv_grammar.productions())

rd = RecursiveDescentParser(oblv_grammar)
obliv = 'My life is drab and wretched by comparison'.split()
for x in rd.parse(obliv):
    print(x)
    x.pretty_print()
