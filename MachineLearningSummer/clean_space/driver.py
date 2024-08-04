from addmore_rulebook_examples import add_examples
from sampledataset import partition_dataset, get_training_data, get_test_data
from classification import batch_classify, build_portfolio
import os
from Clients.Utilities.FileUtilities import write_dict_to_csv_in_dir, readjson, write_tojson
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
    # test_data_path = write_dict_to_csv_in_dir(core, 'test_data.csv', test_list, ['label', 'article'])
    # os.system(f'wc -w {current_dir}/{new_rbk_path} {test_data_path} > {core}/wc_stats.txt')

    # print(f'Check: {core}/wc_stats.txt\nContains word count stats\n')
    # time.sleep(0.2)    
    return core

train_n = 0
test_n = 4

dataset_path = r'MachineLearningSummer/fallacy_dataset/datasets/70%_of_dataset.csv'
forbidden_examples = readjson(r'MachineLearningSummer/rulebook_intermediates/examples.json')
train_data: dict = readjson(r'MachineLearningSummer/clean_space/response_bank/batch4/train_data.json')
# test_data: dict = readjson(r'MachineLearningSummer/clean_space/response_bank/batch4/test_data.json')
select_labels = {'<IR>', '<FE>', '<RR>', '<G>', '<DEP>', '<FU>', '<WCB>'}
test_data = {label:[] for label in select_labels}
indexes: dict = readjson(r'MachineLearningSummer/clean_space/response_bank/batch4/indexes.json')
# select_labels = {'<FU>', '<DEP>', '<RR>'}

extra_train_data, updated_indexes = get_training_data(dataset_path, train_n, indexes, forbidden_examples, select_labels)
for label in extra_train_data:
    if label in train_data:
        train_data[label] += extra_train_data[label]
    else:
        train_data[label] = extra_train_data[label]

extra_test_data, updated_indexes = get_test_data(dataset_path, test_n, indexes, forbidden_examples)
indexes.update(updated_indexes)

count = 0
for label in extra_test_data:
    test_data[label] += extra_test_data[label]
    count += len(test_data[label])
    # print(f'{label} count: ', len(test_data[label]))
print('count: ', count)
# print(test_data)
# c = input()
write_tojson(r'MachineLearningSummer/clean_space/response_bank/batch34/indexes.json', indexes)
write_tojson(r'MachineLearningSummer/clean_space/response_bank/batch34/test_data.json', test_data)
write_tojson(r'MachineLearningSummer/clean_space/response_bank/batch34/train_data.json', train_data)

# new_path = r'MachineLearningSummer/rule_book_bank'
# name = 'RAW_RuleBooks'
rbk_path = r'MachineLearningSummer/rule_book_bank/RAW_RuleBooks_36.txt'
portfolio_dir = r'MachineLearningSummer/clean_space/Portfolios'
portfolio_name = r'portfolio2.txt'

# new_rbk_path = add_examples(train_data, rbk_path, new_path, name)
new_rbk_path = rbk_path
decision = input('Continue? [Y]/[n]: ')
if decision == 'Y' or decision == 'y':
    print('running...')
    batch_dir = r"MachineLearningSummer/clean_space/response_bank/batch34"
    article_to_label_map = {}
    for label in test_data:
        for article in test_data[label]:
            article_to_label_map[article] = label
    batch_classify(rbk_path=new_rbk_path, article_to_label_map=article_to_label_map, batch_dir=batch_dir)

# article_to_label_map = {}
# for label in test_data:
#     for article in test_data[label]:
#         article_to_label_map[article] = label
# # print(article_to_label_map)
# print(build_portfolio(rbk_path=rbk_path, article_to_label_map=article_to_label_map, portfolio_dir=portfolio_dir, portfolio_name='portfolio2'))