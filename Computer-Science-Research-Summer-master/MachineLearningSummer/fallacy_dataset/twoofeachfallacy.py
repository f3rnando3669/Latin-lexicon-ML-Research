import pandas as pd

df = pd.read_csv(r'fallacy_dataset/final_filter.csv')
combine = zip(df['label'].to_list(), df['article'].to_list())
d = {}

for label, article in combine:
    if label in d:
        if len(d[label]) == 2:
            continue
        d[label].append(article)
    else:
        d[label] = [article]

inverted_d = {}
for label in d:
    for article in d[label]:
        if article in inverted_d:
            continue
        inverted_d[article] = label

import json

fd = open(r'', 'w+')
json_object = json.dump(inverted_d, fd)
fd.close()
