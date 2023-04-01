import nltk
from nltk import CFG, RecursiveDescentParser, TreePrettyPrinter
from nltk.tree import *

categoryGrammar = nltk.data.load('file:Categrammar.cfg')

csent = "The striped cat was lying in the field yesterday".split()

c_parser = nltk.RecursiveDescentParser(categoryGrammar)
for tree in c_parser.parse(csent):
    #print(tree); 
    tree.pretty_print() 

