import os
import numpy as np
from scipy.sparse import coo_array

# Global Variables
PATH = os.path.dirname(__name__)
indexed_Trigrams = {}
indexed_Genes = {}
geneIndex = 0
trigramIndex = 0

trigram_coordinates = np.array([]) #row coordinate
gene_coordinates = np.array([]) #column coordinate
data = np.array([])

gene_matrix = coo_array((trigramIndex, geneIndex), dtype=int)

def core_Process(dirName):
    # Directory Name -> no output
    for file in os.listdir(os.path.join(PATH, dirName)):
        if not file.startswith('.'):
            realFile = dirName + "/" + file
            #print("currently working on file {}".format(realFile))
            FASTA_reader(os.path.join(PATH, realFile))
    """
    Debugging print()s
    print(trigram_coordinates)
    print(gene_coordinates)
    print(data)
    """
    matrix_factory()
    return

def matrix_factory():
    # no input -> no return type
    # prints the finalized array that we are working on
    gene_matrix = coo_array((data, (trigram_coordinates, gene_coordinates)), shape=(trigramIndex, geneIndex))
    print(gene_matrix.toarray())

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

def array_Update(tri_coord):
    # int -> no return type
    # this updates all 3 arrays that make up our matrix
    global data, gene_coordinates, trigram_coordinates
    data = np.insert(data, len(data),1)
    #print("I am placing {} in the data array".format(1))

    gene_coordinates = np.append(gene_coordinates, [(geneIndex-1)])
    #print("I am placing {} in the gene_coordinates array".format((geneIndex-1)))

    # trigram_coordinates is the only one that should be moving around a lot
    trigram_coordinates = np.append(trigram_coordinates, [tri_coord])
    #print("I am placing {} in the trigram_coordinates array".format(tri_coord))
    return

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
    if indexed_Trigrams.get(trigram) is None:
        # in the case of a new trigram
        indexed_Trigrams.update({trigram: trigramIndex})
        array_Update(trigramIndex)
        trigramIndex += 1
    else:
        # in the case of a duplicate
        array_Update(indexed_Trigrams.get(trigram))

####################### TESTING FUNCTIONS #######################
def my_testing():
    # Testing function that serves no purpose anymore
    core_Process("testSequences")
    print(indexed_Trigrams)
    print(indexed_Genes)

    #print(gene_matrix.toarray())

    #trigram_scan(trial2['sequence'])
    #print(trial['sequence'])
    return
def messing_with_matricies():
    # no input -> no return type
    # just used to figure out how matrices function. No real purpose but being left for future developement sake
    working_matrix = coo_array((data, (trigram_coordinates, gene_coordinates)), shape=(4, 2))
    print(working_matrix.toarray())
    return

core_Process("bad_boys_FASTA")
print(indexed_Trigrams)
print(indexed_Genes)
print(geneIndex)
print(trigramIndex)
