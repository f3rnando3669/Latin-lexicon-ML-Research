from Bio import Entrez, SeqIO
import os

# Set your email here
Entrez.email = "your-email@example.com"

# Function to search for proteins by organism
def search_proteins(organism_query):
    search_handle = Entrez.esearch(db="protein", term=organism_query, retmax=20)
    search_results = Entrez.read(search_handle)
    search_handle.close()
    return search_results["IdList"]

# Function to fetch and save protein sequences
def fetch_protein_sequences(protein_ids, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for index, protein_id in enumerate(protein_ids, start=1):
        fetch_handle = Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text")
        protein_sequence = fetch_handle.read()
        fetch_handle.close()
        
        output_file_path = os.path.join(output_directory, f"SbRG{index}.txt")
        
        with open(output_file_path, "w") as output_file:
            output_file.write(f"Protein ID: {protein_id}\nProtein Sequence:\n{protein_sequence}\n")
        
        print(f"Saved {output_file_path}")

# Main function to execute the search and fetch operations
def main():
        # Include chromosome information in the search query
    chromosome = "1"  # Specify the chromosome of interest
    organism_query = f"txid4558[organism:exp] AND {chromosome}[chr]"
    protein_ids = search_proteins(organism_query)
    output_directory = "C:\\Users\\mcjal\\OneDrive\\Documents\\python\\ProteinSeq"
    fetch_protein_sequences(protein_ids, output_directory)

# Run the main function
if __name__ == "__main__":
    main()
