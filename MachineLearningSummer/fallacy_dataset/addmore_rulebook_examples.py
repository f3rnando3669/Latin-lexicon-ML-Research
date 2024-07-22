import pandas as pd
from Utilities.FileUtilities import read_filelines, write_lines, readjson
import re

path = r'MachineLearningSummer/fallacy_dataset/70%_of_dataset.csv'
df = pd.read_csv(path)
labels = df['label'].loc[::-1]
articles = df['article'].loc[::-1]

targets_path = r'MachineLearningSummer/fallacy_dataset/abrev_to_fallacy.json'
targets = readjson(targets_path)
# targets = {'<WCB>'}
rv = {target:[] for target in targets}
# print(rv)
# fash = 0
for label, article in zip(labels, articles):
    if label in targets:
        # if fash < 6:
            # fash += 1
            # continue
        # if len(rv[label]) == 2:
            # break
        rv[label].append(article)

rb_path = r'MachineLearningSummer/rulebook_intermediates/rulebk_21_intermediary.txt'
rbk = read_filelines(rb_path)


for target in targets:
    for i, definition in enumerate(rbk):
        if re.match(r'^Define '+target, definition):
            definition = definition.rstrip().removesuffix(")")
            new_examples = []
            for example in rv[target]:
                new_examples.append(f"\"{example}\"")
            new_examples_str = ", ".join(new_examples)
            definition += ", " + new_examples_str +")\n"
            rbk[i] = definition

new_path = r'MachineLearningSummer/rulebook_intermediates/rulebk_21.txt'
write_lines(new_path, rbk)