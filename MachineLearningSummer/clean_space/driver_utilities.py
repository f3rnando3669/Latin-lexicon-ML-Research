import os
import re
from Clients.Utilities.FileUtilities import write_tojson

current_dir = os.getcwd()
clean_space_dir = f'{current_dir}/MachineLearningSummer/clean_space/'
rule_book_bank_path = r'MachineLearningSummer/rule_book_bank'

def get_rulebook_bank_path() -> str:
    return rule_book_bank_path

def get_clean_space_dir() -> str:
    return clean_space_dir

def generate_batch_directory(pattern=r'batch[0-9]+'):    
    directories = os.listdir(f'{clean_space_dir}response_bank')
    count = 1
    for directory in directories:
        if re.match(pattern, directory):
            count += 1
    working_dir = f'{clean_space_dir}response_bank/batch{count}'
    os.system(f'mkdir -p {working_dir}')
    return working_dir

# def count_words(paths, write_path) -> str:
#     argument = "wc -w"
#     for path in paths:
#         argument += ' ' + path
#     os.system(argument)
#     print(f'Check: {write_path}/wc_stats.txt\nContains word count stats\n')
#     return f'{working_dir}/wc_stats.txt'

def update_data(data_dict:dict, new_data:dict) -> dict:
    for label in new_data:
        if label in data_dict:
            data_dict[label] += new_data[label]
        else:
            data_dict[label] = new_data[label]
    return data_dict

def build_article_label_map(data_dict:dict):
    article_to_label_map = {}
    for label in data_dict:
        for article in data_dict[label]:
            article_to_label_map[article] = label
    return article_to_label_map

def write_experiment_info(working_dir:str, data_dicts:list) -> None:
    if working_dir[-1] != '/':
        working_dir += '/'
    for name, data_dict in data_dicts:
        write_tojson(f'{working_dir}{name}.json', data_dict)