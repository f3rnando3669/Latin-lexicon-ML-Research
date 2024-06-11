"""
Might use this code at some point as a feature of the whole.
"""
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

def RNA_check(strand):
    # string -> string
    # checks if a strand contains an amino acid, if it does translate it over to a protein chain
    if not strand.contains("M"):
        protein = translation(strand)
        return protein
    else:
        return strand

def translation(strand):
    # String  -> String
    # function that changes an RNA strand to its Amino Acid Chain
    AAseq = ""
    for i in range(0, len(strand), 3):
        codon = strand[i:i + 3]
        AAseq += (codonChart[codon])
    return AAseq