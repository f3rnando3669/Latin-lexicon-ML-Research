import pandas as pd
import csv

original_path = r'MachineLearningSummer/fallacy_dataset/final_filter.csv'
df = pd.read_csv(original_path)
original_entries = zip(df['article'].to_list(), df['label'].to_list())
original_table = {article:label for article,label in original_entries}
# print(original_table)

filtered_path = r'MachineLearningSummer/fallacy_dataset/70%_of_dataset.csv'
df1 = pd.read_csv(filtered_path)
filtered_entries = zip(df1['article'].to_list(), df1['label'].to_list())
filtered_table = {article:label for article,label in filtered_entries}
# entries = []

table = []
for article in original_table:
    if article in filtered_table:
        continue
    table.append({'label':original_table[article], 'article':article})

# print(df2)
# print(table)
fd = open(r'MachineLearningSummer/fallacy_dataset/30%_of_dataset.csv', 'w')
writer = csv.DictWriter(fd, fieldnames=['label', 'article'])
writer.writeheader()
writer.writerows(table)
fd.close()