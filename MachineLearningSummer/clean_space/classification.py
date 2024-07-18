from Clients.ClientInterface import ClientInterface
from Clients.ContextTightClient import ContextTightClient
from Prompts.SimplePrompt import SimplePrompt
from Prompts.PromptList import PromptList
from Clients.Utilities.FileUtilities import readfile, readjson, write_to_file_in_dir
from extract import iscorrect

# Classification Experiment
rulebook_path = r"Computer-Science-Research-Summer/MachineLearningSummer/rule_book_bank/RAW_Rulebooks_18.txt"
params = readfile(rulebook_path)
param_prompt = SimplePrompt(params)
mapping_path = r"Computer-Science-Research-Summer/MachineLearningSummer/fallacy_dataset/article_to_label_test.json"
article_to_label_map = readjson(mapping_path)
# print(article_to_label_map)
# target = ['<FU>', '<WCB>']
response_paths = []
for article in article_to_label_map:
        prompt = SimplePrompt(f"Apply <IDAA> to \"{article}\"")
        prompts = PromptList()
        prompts.add_userprompts([param_prompt, prompt])
        client_interface = ClientInterface(ContextTightClient)
        tpath = r"Computer-Science-Research-Summer/MachineLearningSummer/clean_space/response_bank"
        response = client_interface._client.generate(prompts=prompts)
        txt_name = article_to_label_map[article][1:-1]
        path = write_to_file_in_dir(tpath, txt_name, response)
        response_paths.append(path)

dir = r"Computer-Science-Research-Summer/MachineLearningSummer/clean_space/response_bank/"
count = 0
total = 0
for path in response_paths:
    correct, num =  iscorrect(dir+path)
    if correct:
        count += 1
    total += num

print(f'Correctly Indentified: {count}\nPercentage: {count/total*100}')