import pandas as pd
from Clients.Utilities.FileUtilities import read_filelines, readjson, write_lines_to_dir
import re
from dataset_utils import get_labels_and_articles, get_limited_labels_and_articles


def add_examples(tag_to_article:dict, rbk_path:str, dir:str, name:str, prefix=r'^Define ', suffix=r')') -> str:
    rbk = read_filelines(rbk_path)

    for tag in tag_to_article:
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

# dataset_path = r'MachineLearningSummer/fallacy_dataset/datasets/20%_of_70%_of_dataset.csv'
# tags_path = r'MachineLearningSummer/fallacy_dataset/abrev_to_fallacy.json'
# rb_path = r'MachineLearningSummer/rule_book_bank/RAW_RuleBooks_22.txt'
# new_path = r'MachineLearningSummer/rule_book_bank'
# name = 'RAW_RuleBooks'
# add_examples(dataset_path=dataset_path, tags_path=tags_path, rbk_path=rb_path, dir=new_path, name=name, limit=5)