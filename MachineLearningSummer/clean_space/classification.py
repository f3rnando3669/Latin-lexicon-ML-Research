from Clients.ClientInterface import ClientInterface
from Clients.ContextTightClient import ContextTightClient
from Prompts.SimplePrompt import SimplePrompt
from Prompts.PromptList import PromptList
from Clients.Utilities.FileUtilities import readfile, readjson, write_to_file_in_dir, readcsv
from extract import iscorrect
# import csv

# Classification Experiment
rulebook_path = r"MachineLearningSummer/rule_book_bank/RAW_RuleBooks_21.txt"
params = readfile(rulebook_path)
param_prompt = SimplePrompt(params)
mapping_path = r"MachineLearningSummer/fallacy_dataset/article_to_label_test.json"
dataset = readcsv(r'MachineLearningSummer/fallacy_dataset/30%_of_dataset.csv')
# print(dataset)
article_to_label_map = {}
for entry in dataset:
    label, article = entry
    article_to_label_map[article] = label
# print(len(article_to_label_map))
# print(article_to_label_map)
# article_to_label_map = readjson(mapping_path)
# print(article_to_label_map)
# target = ['<WCB>']
response_paths = []
for article in article_to_label_map:
        # if article_to_label_map[article] in target:
        prompt = SimplePrompt(f"Apply <IDAA> to \"{article}\"")
        prompts = PromptList()
        prompts.add_userprompts([param_prompt, prompt])
        client_interface = ClientInterface(ContextTightClient)
        tpath = r"clean_space/response_bank/batch1"
        response = client_interface._client.generate(prompts=prompts)
        txt_name = article_to_label_map[article][1:-1]
        path = write_to_file_in_dir(tpath, txt_name, response)
        response_paths.append(path)

# dir = r"clean_space/response_bank/"
count = 0
total = 0
for path in response_paths:
    correct, num =  iscorrect(path)
    if correct:
        count += 1
    total += num

print(f'Correctly Indentified: {count}\nPercentage: {count/total*100}')