"""
AUTHOR: Sebastian Gutierrez-Olvera
GITHUB: Sebas-2000
DATE CREATED: 6/28/2023
DATE LAST MODIFIED: 6/14/2024
NOTE: Might use this code at some point as a tool for analysis
"""
codon_chart: dict = {
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
protein_letter_to_name: dict = {
    "P": "Proline", "A": "Alanine", "I": "Isoleucine", "L": "Leucine", "M": "Methionine", "G": "Glycine", "V": "Valine", # Nonpolar Aliphatic Amino Acids
    "W": "Tryptophan", "Y": "Tyrosine", "F": "Phenylalanine", # Nonpolar Aromatic Amino Acids
    "H": "Histidine", "R": "Arginine", "K": "Lysine", # Positively Charged Polar Amino Acids
    "C": "Cysteine", "S": "Serine", "T": "Threonine", "Q": "Glutamine", "N": "Asparagine",# Polar Amino Acids
    "E": "Glutamic_Acid", "D": "Aspartic_Acid" # Negatively Charged Polar Amino Acids
}
protein_letter_to_code: dict = {
    "P": "Pro", "A": "Ala", "I": "Ile", "L": "Leu", "M": "Met", "G": "Gly", "V": "Val", # Nonpolar Aliphatic Amino Acids
    "W": "Trp", "Y": "Tyr", "F": "Phe", # Nonpolar Aromatic Amino Acids
    "K": "Lys", "R": "Arg", "H": "His", # Positively Charged Polar Amino Acids
    "C": "Cys", "S": "Ser", "T": "Thr", "N": "Asn", "Q": "Gln", # Polar Amino Acids
    "E": "Glu", "D": "Asp"
}

test_sequence: str = "MPNLWCETFAHIDGSYQKVR"

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
        AAseq += (codon_chart[codon])
    return AAseq

def expand_sequence(seq) -> str:
    return_seq: str = ""
    for i in range(0, len(seq)):
         return_seq += (protein_letter_to_code[i])
    return return_seq

def main():
    print(expand_sequence(test_sequence))
    return

if __name__ == '__main__':
    main()