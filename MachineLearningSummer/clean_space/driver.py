from addmore_rulebook_examples import add_examples
from sampledataset import get_new_data
from classification import batch_classify, build_portfolio, batch_classify_with_portfolio
from driver_utilities import update_data, generate_batch_directory, write_experiment_info, build_article_label_map, get_rulebook_bank_path, get_clean_space_dir
from Clients.Utilities.FileUtilities import readjson

def experiment(train_n:int, test_n:int, dataset_path, rbk_path, create_new_rbk=False, portfolio=False, portfolio_path="", forbidden_examples={}, train_data={}, test_data={}, indexes={}, select_labels={}) -> str:
    """
    run a classification experiment\n
    returns summary path
    """
    if portfolio:
        if not portfolio_path:
            raise Exception("No portfolio path defined")
    extra_train_data, updated_indexes = get_new_data(dataset_path, train_n, indexes, forbidden_examples, select_labels)
    train_data = update_data(data_dict=train_data, new_data=extra_train_data)
    extra_test_data, updated_indexes = get_new_data(dataset_path, test_n, indexes, forbidden_examples, select_labels)
    indexes.update(updated_indexes)
    test_data = update_data(data_dict=test_data, new_data=extra_test_data)
    working_directory = generate_batch_directory()
    write_experiment_info(working_dir=working_directory, data_dicts=[('indexes', indexes), ('test_data', test_data), ('train_data', train_data)])
    
    if create_new_rbk:
        rbk_path = add_examples(train_data, rbk_path, rule_book_bank_path, 'RAW_RuleBooks')
    article_to_label_map = build_article_label_map(test_data)
    
    decision = input('Continue? [Y]/[n]: ')
    summary = ""
    if decision == 'Y' or decision == 'y':
        if portfolio:
            print('classifying with portfolio...')
            summary = batch_classify_with_portfolio(rbk_path=rbk_path, portfolio_path=portfolio_path, article_to_label_map=article_to_label_map, batch_dir=working_directory)
        else:
            print('classifying...')
            summary = batch_classify(rbk_path=rbk_path, article_to_label_map=article_to_label_map, batch_dir=working_directory)
    print("Experiment complete!")
    return summary

def create_portfolio(portfolio_dir:str, portfolio_name:str, dataset_path:str, rbk_path:str, data_dict:dict, example_count:int, indexes={}, forbidden_examples={}, select_labels={}) -> str:
    """
    create a portfolio\n
    returns portfolio path
    """
    extra_data,_ = get_new_data(dataset_path, example_count, indexes, forbidden_examples, selected=select_labels)
    data_dict = update_data(data_dict=data_dict, new_data=extra_data)
    article_to_label_map = build_article_label_map(data_dict)
    decision = input('Continue? [Y]/[n]: ')
    if decision == 'Y' or decision == 'y':
        print('building portfolio...')
        portfolio_path = build_portfolio(rbk_path=rbk_path, article_to_label_map=article_to_label_map, portfolio_dir=portfolio_dir, portfolio_name=portfolio_name)
        print('Portfolio complete!')
    return portfolio_path

train_n = 0
test_n = 4
clean_space_dir = get_clean_space_dir()
dataset_path = r'MachineLearningSummer/fallacy_dataset/datasets/70%_of_dataset.csv'
forbidden_examples = readjson(r'MachineLearningSummer/rulebook_intermediates/examples.json')
# train_data: dict = readjson(clean_space_dir+r'/response_bank/batch4/train_data.json')
# test_data: dict = readjson(clean_space_dir+r'response_bank/batch4/test_data.json')
# indexes: dict = readjson(clean_space_dir+r'/response_bank/batch4/indexes.json')
select_labels = {'<IR>', '<FE>', '<RR>', '<G>', '<DEP>', '<FU>', '<WCB>'}
indexes = {label:0 for label in select_labels}
rule_book_bank_path = get_rulebook_bank_path()
rbk_path = f'{rule_book_bank_path}/RAW_RuleBooks_44.txt'

experiment(train_n=train_n, test_n=test_n, dataset_path=dataset_path, rbk_path=rbk_path, forbidden_examples=forbidden_examples, indexes=indexes, select_labels=select_labels)
