import requests
import os

base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

organism_query = "txid4558[organism:exp]"
search_url = f"{base_url}esearch.fcgi?db=protein&term={organism_query}&retmode=json"

# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=protein&term=txid4558[organism:exp]&retmode=json
response = requests.get(search_url)
search_results = response.json()

protein_ids = search_results["esearchresult"]["idlist"]

output_directory = "proteinSeq"

# os.makedirs(output_directory, exist_ok=True)

i = 0
for protein_id in protein_ids:
    fetch_url = f"{base_url}efetch.fcgi?db=protein&id={protein_id}&rettype=fasta&retmode=text"
    protein_sequence = requests.get(fetch_url).text

    # Create a separate text file for each protein sequence
    output_file_path = os.path.join(output_directory, f"protein_{protein_id}.txt")

    print(f'output director is {output_directory}')

    with open(output_file_path, "w") as output_file:
        output_file.write(f"Protein ID: {protein_id}\nProtein Sequence:\n{protein_sequence}\n")
        # print(f'{i}: file {protein_id} saved')
        print(
            f"protein_{protein_id}.txt")

    i += 1
    if i > 5:
        break
