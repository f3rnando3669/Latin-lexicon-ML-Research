from addmore_rulebook_examples import add_examples
from sampledataset import partition_dataset
from classification import batch_classify
import os
from Clients.Utilities.FileUtilities import write_dict_to_csv_in_dir
import time
import re

def cli_stuff() -> str:
    current_dir = os.getcwd()
    dirs = os.listdir(f'{current_dir}/MachineLearningSummer/clean_space/response_bank')
    count = 1
    for dir in dirs:
        if re.match(r'batch[0-9]+', dir):
            count += 1

    core = current_dir+f'/MachineLearningSummer/clean_space/response_bank/batch{count}'
    os.system(f'mkdir -p {core}')
    test_data_path = write_dict_to_csv_in_dir(core, 'test_data.csv', test_list, ['label', 'article'])
    os.system(f'wc -w {current_dir}/{new_rbk_path} {test_data_path} > {core}/wc_stats.txt')

    print(f'Check: {core}/wc_stats.txt\nContains word count stats\n')
    time.sleep(0.2)    
    return core

train_n = 2
test_n = train_n
dataset_path = r'MachineLearningSummer/fallacy_dataset/datasets/70%_of_dataset.csv'
training_data, test_data, test_list = partition_dataset(dataset_path, train_n, test_n)

rbk_path = r'MachineLearningSummer/rulebook_intermediates/RAW_template.txt'
new_path = r'MachineLearningSummer/rule_book_bank'
name = 'RAW_RuleBooks'
new_rbk_path = add_examples(tag_to_article=training_data, rbk_path=rbk_path, dir=new_path, name=name, limit=train_n)
batch_dir = cli_stuff()
decision = input('Continue? [Y]/[n]: ')
if decision == 'Y' or decision == 'y':
    print('testing...')
#     # batch_dir = r"MachineLearningSummer/clean_space/response_bank/batch4"
#     # batch_classify(rbk_path=new_rbk_path, dataset=test_data, batch_dir=batch_dir)