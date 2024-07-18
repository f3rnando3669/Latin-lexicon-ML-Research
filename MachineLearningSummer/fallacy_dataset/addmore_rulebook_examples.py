import pandas as pd
from Utilities.FileUtilities import read_filelines, write_lines
import re

path = r'fallacy_dataset/final_filter.csv'
df = pd.read_csv(path)
labels = df['label'].loc[::-1]
articles = df['article'].loc[::-1]

targets = {'<WCB>'}
rv = {target:[] for target in targets}

for label, article in zip(labels, articles):
    if label in targets:
        if len(rv[label]) == 2:
            break
        rv[label].append(article)

rb_path = r''
rbk = read_filelines(rb_path)


for target in targets:
    for i, definition in enumerate(rbk):
        if re.match(f'Define {target}'+r'[a-zA-Z0-9\s]*', definition):
            definition = definition.rstrip().removesuffix(")")
            new_examples = []
            for example in rv[target]:
                new_examples.append(f"\"{example}\"")
            new_examples_str = ", ".join(new_examples)
            definition += ", " + new_examples_str +")\n"
            rbk[i] = definition

new_path = r''
write_lines(new_path, rbk)
