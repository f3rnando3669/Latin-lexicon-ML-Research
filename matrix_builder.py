import pandas as pd
import numpy as np
from scipy.sparse import coo_array

# Global Variables
existing_trigrams = {}
genes_in_order = [] # might use for later purposes
trigram_index: int = 0
gene_index: int = 0
row_coordinates = np.array([]) # trigrams
column_coordinates = np.array([]) # genes
data = np.array([])


# Step 1: Read the csv file using pandas
def pd_reader(file_name: str) -> pd.DataFrame:
    # df = pd.read_csv("snap.csv",names =["x", "y", "z", "vx", "vy", "vz"])
    df = pd.read_csv(file_name, names=["Locus", "Accession ID", "Protein Name", "Organism", "Sequence"])
    df = df.loc[:, ['Locus', 'Sequence']] # excludes the other columns
    df.drop(0, axis=0, inplace=True)
    return df


# Step 2 Pull data from Pandas dataframe as name and sequence by row
def pull_data(df: pd.DataFrame) -> None:
    for index, row in df.iterrows():
        # Increment gene_index per gene read through
        global gene_index
        gene_index += 1

        # Pull the name and sequence from the dataframe
        name = row['Locus']
        sequence = row['Sequence']

        # for each gene, grab and index the trigrams
        #print(name, sequence)
        genes_in_order.append(name)
        trigram_maker(sequence)
    return
    

# Step 3: Break the sequence into trigrams
def trigram_maker(sequence: str) -> None:
    for i in range(1, (len(sequence)-2)):
        tempTrigram = sequence[i] + sequence[(i+1)] + sequence[(i+2)]
        #print(tempTrigram + "\n")
        trigram_manager(tempTrigram)
    return


# Step 4: Sort trigrams and deal with them accordingly
def trigram_manager(trigram: str) -> None:
    global trigram_index
    if existing_trigrams.get(trigram) is None:
        # in the case of a new trigram
        existing_trigrams.update({trigram: trigram_index})
        array_manager(trigram_index)
        trigram_index += 1
    else:
        # in the case of a duplicate
        array_manager(existing_trigrams.get(trigram))
        pass
    return


# Step 5: update the 3 arrays that build the matrix as needed
def array_manager(trigram_coor: int) -> None:
    # this updates all 3 arrays that make up our matrix
    global data, column_coordinates, row_coordinates
    data = np.insert(data, len(data),1)
    #print("I am placing {} in the data array".format(1))

    column_coordinates = np.append(column_coordinates, [(gene_index-1)])
    #print("I am placing {} in the gene_coordinates array".format((geneIndex-1)))

    # trigram_coordinates is the only one that should be moving around a lot
    row_coordinates = np.append(row_coordinates, [trigram_coor])
    #print("I am placing {} in the trigram_coordinates array".format(tri_coord))
    return


# Step 6: Finally make the matrix
def matrix_maker() -> coo_array:
    matrix = coo_array((data, (row_coordinates, column_coordinates)), shape=(trigram_index, gene_index))
    return matrix


def main(data_set_name: str) -> coo_array:
    # Create blank matrix that will be filled in
    gene_matrix = coo_array((trigram_index, gene_index), dtype=int)
    # Read the csv file
    df_main = pd_reader(data_set_name)
    # Break the data down and populate the 3 arrays
    pull_data(df_main)
    # Re-Assign the matrix with the new data
    gene_matrix = matrix_maker()
    # Print the matrix
    print(gene_matrix.toarray())
    return gene_matrix


if __name__ == "__main__":
    main("good_boys.csv")
    print(trigram_index)