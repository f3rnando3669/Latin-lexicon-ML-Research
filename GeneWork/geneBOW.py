import os
import numpy as np
import scipy as sp


# Global Variables
PATH = os.path.dirname(__name__)

def FASTA_Reader(file):
    # FASTA_file.txt -> dictionary
    # reads a FASTA file.txt and separates the Name line from the actual sequence.
    # Also joins the sequence together
    working_file = open(file, "r")
    #nameTag = working_file.readline().replace('\n',"")
    rv = {'geneName': working_file.readline().replace('\n',""), 'sequence': ""}
    AAseq = ""
    for line in working_file:
            AAseq += line.replace("\n",'')
    rv.update({'sequence':AAseq})
    return rv

trial = FASTA_Reader(os.path.join(PATH, "geneSequences/SbST1.txt"))
print(trial)