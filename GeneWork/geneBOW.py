import os
import numpy as np
from scipy.sparse import coo_array

# Global Variables
PATH = os.path.dirname(__name__)
indexed_Trigrams = {}
indexed_Genes = {}
geneIndex = 0
trigramIndex = 0

def core_Process():
    # no input -> no output
    # this is the MAIN process for what we are doing. Built because FASTA_reader() got too big
    FASTA_reader()
    return
def messing_With_Matricies():
    # no input -> no return type
    # this is just going to print out a matrix as I work on it to get accustomed
    row_of_genes = np.array([])
    column_of_proteins = np.array([])
    working_Matrix = coo_array((3, 4), dtype=int)

    return
def FASTA_reader(file):
    # FASTA_file.txt -> dictionary
    # reads a FASTA file.txt and separates the Name line from the actual sequence.
    working_file = open(file, "r", encoding='utf-8-sig')
    rv = {'geneName': working_file.readline().replace('\n', ""), 'sequence': ""}
    sequence = ""
    # Combine lines together
    for line in working_file:
        sequence += line.replace("\n", '')
    # Update appropriate dictionaries
    rv.update({'sequence': sequence})
    gene_indexing(rv['geneName'])
    trigram_scan(rv["sequence"])

    working_file.close()
    return rv

def gene_indexing(gene):
    # string, integer -> no return
    # adds genes that have been read to indexing dictionary
    global geneIndex
    indexed_Genes.update({gene: geneIndex})
    geneIndex += 1

def trigram_scan(proteinChain):
    # string -> no return type
    # runs through an amino acid chain and breaks it into trigrams while indexing them in indexed_Trigrams
    for i in range(0, (len(proteinChain)-2)):
        tempTrigram = proteinChain[i] + proteinChain[(i+1)] + proteinChain[(i+2)]
        trigram_indexing(tempTrigram)

def trigram_indexing(trigram):
    # string -> no return type
    # function that adds trigrams that have not been seen to indexed_Trigrams and updates counter
    global trigramIndex
    if indexed_Trigrams.get(trigram) == None:
        indexed_Trigrams.update({trigram: trigramIndex})
        trigramIndex += 1
    else:
        #print("Trigram: {} already exists".format(trigram))
        pass


def my_testing():
    # Testing
    FASTA_reader(os.path.join(PATH, "geneSequences/TEST_1.txt"))
    FASTA_reader(os.path.join(PATH, "geneSequences/TEST_2.txt"))
    #print(trial2)
    #trial3 = FASTA_reader(os.path.join(PATH, "geneSequences/SbST3.txt"))
    #print(trial3)
    #trigram_scan(trial['sequence'])
    print(indexed_Trigrams)
    print(indexed_Genes)

    print(working_Matrix.toarray())

    #trigram_scan(trial2['sequence'])
    #print(trial['sequence'])

my_testing()