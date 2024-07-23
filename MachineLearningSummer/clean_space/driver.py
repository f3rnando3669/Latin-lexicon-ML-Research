from addmore_rulebook_examples import add_examples
from sampledataset import partition_dataset
from classification import batch_classify

n = 2
dataset_path = r'MachineLearningSummer/fallacy_dataset/datasets/70%_of_dataset.csv'
training_data, test_data = partition_dataset(dataset_path, n)
# print(training_data)
# tags_path = r'MachineLearningSummer/fallacy_dataset/abrev_to_fallacy.json'
rbk_path = r'MachineLearningSummer/rulebook_intermediates/rulebk_21_intermediary.txt'
new_path = r'MachineLearningSummer/rule_book_bank'
name = 'RAW_RuleBooks'
new_rbk_path = add_examples(dataset_path=dataset_path, tags_path=training_data, rbk_path=rbk_path, dir=new_path, name=name, limit=n)

# batch_dir = r"MachineLearningSummer/clean_space/response_bank/batch4"
# batch_classify(rbk_path=new_rbk_path, dataset=test_data, batch_dir=batch_dir)