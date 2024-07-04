import pandas as pd
import numpy as np
from scipy.sparse import coo_array
import os

# Step 1: Read the csv file using pandas
def pd_reader(file_name: str) -> None:
    # df = pd.read_csv("snap.csv",names =["x", "y", "z", "vx", "vy", "vz"])
    df = pd.read_csv(file_name, names=["Locus", "Accession ID", "Protein Name", "Organism", "Sequence"])
    df = df.loc[:, ['Locus', 'Sequence']] # excludes the other columns
    df.drop(0, axis=0, inplace=True)
    print(df)
    # [x] check here if it works with full_sequence_list.csv

# Step 2


def main() -> None:
    pd_reader("test_sequences.csv")

if __name__ == "__main__":
    main()