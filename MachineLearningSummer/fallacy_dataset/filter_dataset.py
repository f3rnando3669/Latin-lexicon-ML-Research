import pandas as pd

# df = pd.read_csv('/home/andi/summer2024/fallacy_dataset/edu_train.csv')
# combine = df[['source_article', 'updated_label']]
# combine.to_csv('filtered_data.csv', header=True, index=False)

# from dataset_filter import DatasetFilter
# fil = DatasetFilter('/home/andi/summer2024/fallacy_dataset/edu_train.csv')
# fil.filter(['updated_label'])
# fil.write_tocsv(name='updated_labelcolumn')

# df = pd.read_csv('/home/andi/summer2024/fallacy_dataset/edu_train.csv')
# combine = df[['updated_label']]
# fd = open('fallacy_dict.txt', 'w')
# fd.write(str(set(combine.to_dict()['updated_label'].values())))
# fd.close()

# from dataset_filter import DatasetFilter
# fil = DatasetFilter('/home/andi/summer2024/fallacy_dataset/edu_all.csv')
# fil.filter(['updated_label', 'source_article'])
# fil.write_tocsv(name='edu_all_filtered')

# import json
# fd = open(r'/home/andi/summer2024/fallacy_dataset/abrev_to_fallacy.json', 'r')
# mapping = json.load(fd)
# fd.close()
# reverse_map = {}
# for letter in mapping:
#     for associates in mapping[letter]:
#         reverse_map[associates] = letter

# fd = open('fallacy_to_abrev.json', 'w')
# json.dump(reverse_map, fd)
# fd.close()

# import json

# fd = open(r'/home/andi/summer2024/fallacy_dataset/fallacy_to_abrev.json', 'r')
# mapping = json.load(fd)
# fd.close()

# df = pd.read_csv(r"/home/andi/summer2024/fallacy_dataset/edu_all_filtered.csv", encoding='utf-8')
# labels = df.loc[:].to_dict()['updated_label']
# articles = df.loc[:].to_dict()['source_article']
# col_names = ['label', 'article']
# table = []
# for i in range(len(labels)):
#     label = labels[i]
#     article = articles[i]
    
#     if label in mapping:
#         table.append({'label': mapping[label], 'article': article})

# import csv
# fd = open('final_filter.csv', 'w')
# writer = csv.DictWriter(fd, fieldnames=col_names)
# writer.writeheader()
# writer.writerows(table)
# fd.close()

