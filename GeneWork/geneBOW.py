import os
import numpy as np
import scipy as sp

# Global Variables
PATH = os.path.dirname(__name__)
codonChart = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "TCT": "S", "TCC": "S", "TCA": "S",
    "TCG": "S", "TAT": "Y", "TAC": "Y", "TAA": "X", "TAG": "X", "TGT": "C", "TGC": "C",
    "TGA": "X", "TGG": "W", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", "CCT": "P",
    "CCC": "P", "CCA": "P", "CCG": "P", "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "ATT": "I", "ATC": "I", "ATA": "I",
    "ATG": "M", "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAT": "N", "AAC": "N",
    "AAA": "K", "AAG": "K", "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GTT": "V",
    "GTC": "V", "GTA": "V", "GTG": "V", "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGT": "G", "GGC": "G", "GGA": "G",
    "GGG": "G"
}
indexedTrigrams = {}
indexedGenes = {}
howManyGenes = 0


def FASTA_Reader(file):
    # FASTA_file.txt -> dictionary
    # reads a FASTA file.txt and separates the Name line from the actual sequence.
    # Also joins the sequence together
    working_file = open(file, "r")
    rv = {'geneName': working_file.readline().replace('\n', ""), 'sequence': ""}
    AAseq = ""
    for line in working_file:
        AAseq += line.replace("\n", '')
    rv.update({'sequence': AAseq})
    geneIndexing(rv['geneName'], howManyGenes)
    return rv


def RNA_Check():
    return


def translation(strand):
    AAseq = ""
    return AAseq


def geneIndexing(gene, indexNum):
    # string, integer -> no return
    # adds genes that have been read to indexing dictionary
    indexedGenes.update({gene: indexNum})
    global howManyGenes
    howManyGenes += 1


# Testing
trial = FASTA_Reader(os.path.join(PATH, "geneSequences/SbST1.txt"))
print(trial)
trial2 = FASTA_Reader(os.path.join(PATH, "geneSequences/SbST2.txt"))
print(trial2)
print(indexedGenes)