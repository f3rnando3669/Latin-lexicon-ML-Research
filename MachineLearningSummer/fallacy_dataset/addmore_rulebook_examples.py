import pandas as pd
from Utilities.FileUtilities import read_filelines, write_lines_to_dir, readjson
import re

def get_labels(path):
    df = pd.read_csv(path)
    labels = df['label'].loc[::-1]
    return labels

def get_articles(path):
    df = pd.read_csv(path)
    articles = df['article'].loc[::-1]
    return articles

def get_labels_and_articles(path):
    df = pd.read_csv(path)
    labels = df['label'].loc[::-1]
    articles = df['article'].loc[::-1]
    return zip(labels, articles)

def get_limited_labels_and_articles(tags, labels_and_articles, limit=1):
    tag_to_article = {tag:[] for tag in tags}
    for tag, article in labels_and_articles:
        if tag in tags:
            if len(tag_to_article[tag]) == limit:
                continue
            tag_to_article[tag].append(article)
    return tag_to_article

def add_examples(dataset_path, tags_path, rbk_path, dir, name, prefix=r'^Define ', suffix=r')', limit=1) -> str:
    labels_and_articles = get_labels_and_articles(dataset_path)
    tags = readjson(tags_path)
    tag_to_article = get_limited_labels_and_articles(tags, labels_and_articles, limit)
    rbk = read_filelines(rbk_path)

    for tag in tags:
        for i, definition in enumerate(rbk):
            if re.match(prefix+tag, definition):
                definition = definition.rstrip().removesuffix(suffix)
                new_examples = []
                for example in tag_to_article[tag]:
                    new_examples.append(f"\"{example}\"")
                new_examples_str = ", ".join(new_examples)
                definition += ", " + new_examples_str +f"{suffix}\n"
                rbk[i] = definition
    
    return write_lines_to_dir(dir, name, rbk)

# dataset_path = r'MachineLearningSummer/fallacy_dataset/70%_of_dataset.csv'
# tags_path = r'MachineLearningSummer/fallacy_dataset/abrev_to_fallacy.json'
# rb_path = r'MachineLearningSummer/rulebook_intermediates/rbk22_1.txt'
# new_path = r'MachineLearningSummer/rule_book_bank'
# name = 'RAW_RuleBooks'
# add_examples(dataset_path=dataset_path, tags_path=tags_path, rbk_path=rb_path, dir=new_path, name=name)