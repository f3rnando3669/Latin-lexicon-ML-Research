import pandas as pd
import csv

def get_rest_of_filtered_dataset(original_path, filtered_path, new_path):
    df = pd.read_csv(original_path)
    original_entries = zip(df['article'].to_list(), df['label'].to_list())
    original_table = {article:label for article,label in original_entries}

    df1 = pd.read_csv(filtered_path)
    filtered_entries = zip(df1['article'].to_list(), df1['label'].to_list())
    filtered_table = {article:label for article,label in filtered_entries}

    table = []
    for article in original_table:
        if article in filtered_table:
            continue
        table.append({'label':original_table[article], 'article':article})

    fd = open(new_path, 'w')
    writer = csv.DictWriter(fd, fieldnames=['label', 'article'])
    writer.writeheader()
    writer.writerows(table)
    fd.close()

# original_path = r'MachineLearningSummer/fallacy_dataset/datasets/70%_of_dataset.csv'
# filtered_path = r'MachineLearningSummer/fallacy_dataset/datasets/20%_of_70%_of_dataset.csv'
# new_path = r'MachineLearningSummer/fallacy_dataset/datasets/80%_of_70%_of_dataset.csv'

# get_rest_of_filtered_dataset(original_path=original_path, filtered_path=filtered_path, new_path=new_path)