from Clients.ClientInterface import ClientInterface
from Clients.ContextTightClient import ContextTightClient
from Prompts.SimplePrompt import SimplePrompt
from Prompts.PromptList import PromptList
from Clients.Utilities.FileUtilities import readfile, readjson

# Classification Experiment
rulebook_path = r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/rule_book_bank/RAW_Rulebooks_15.txt"
params = readfile(rulebook_path)
param_prompt = SimplePrompt(params)
mapping_path = r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/fallacy_dataset/article_to_label_test.json"
article_to_label_map = readjson(mapping_path)
# print(article_to_label_map)
for article in article_to_label_map:
    print(article_to_label_map[article])
    prompt = SimplePrompt(f"Apply <IDAA> to \"{article}\"")
    prompts = PromptList()
    prompts.add_userprompts([param_prompt, prompt])
    client_interface = ClientInterface(ContextTightClient)
    tpath = r"/home/andi/summer2024/Computer-Science-Research-Summer/MachineLearningSummer/clean_space/response_bank"
    client_interface._client.generate(prompts=prompts, txt_savepath=tpath, txt_name = article_to_label_map[article])