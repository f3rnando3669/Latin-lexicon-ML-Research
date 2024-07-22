from Clients.ClientInterface import ClientInterface
from Clients.ContextTightClient import ContextTightClient
from Prompts.SimplePrompt import SimplePrompt
from Prompts.PromptList import PromptList
from Clients.Utilities.FileUtilities import readfile, readjson, write_to_file_in_dir, readcsv
from extract import iscorrect

# Classification Experiment
def batch_classify(rbk_path, dataset_path, mapping_path, batch_dir, summary_name='batch_summary'):
    params = readfile(rbk_path)
    param_prompt = SimplePrompt(params)
    # dataset = readcsv(dataset_path)
    # article_to_label_map = {}
    # for entry in dataset:
    #     label, article = entry
    #     article_to_label_map[article] = label
    article_to_label_map = readjson(mapping_path)
    # target = ['<WCB>']
    
    response_paths = []
    for article in article_to_label_map:
            # if article_to_label_map[article] in target:
        prompt = SimplePrompt(f"Apply <IDAA> to \"{article}\"")
        prompts = PromptList()
        prompts.add_userprompts([param_prompt, prompt])
        client_interface = ClientInterface(ContextTightClient)
        response = client_interface._client.generate(prompts=prompts)
        txt_name = article_to_label_map[article][1:-1]
        path = write_to_file_in_dir(batch_dir, txt_name, response)
        response_paths.append(path)

    category_details = {}
    incorrect_list = []
    count = 0
    for path in response_paths:
        category = path.split('/')[-1].split('_')[0]
        if category in category_details:
            category_details[category]['Total'] += 1
        else:
            category_details[category] = {'Total':1, 'Correct':0}

        correct = iscorrect(path)
        if correct:
            count += 1
            if category in category_details:
                category_details[category]['Correct'] += 1
            else:
                category_details[category] = {'Correct':1}
        else:
            incorrect_list.append(path)

    total = len(response_paths)
    summary = f'\nGeneral:\nCorrectly Indentified: {count}\nTotal: {total}\nPercentage: {round(count/total*100, 2)}\n\nBreakdown:'
    for category in category_details:
        correct = category_details[category]['Correct']
        total = category_details[category]['Total']
        summary += f'\n{category}:\nCorrect: {correct}\nTotal: {total}\nPercentage: {correct/total*100}\n'
        summary += "=" * 30
    summary += "\n\nPaths for Incorrect Files:\n"+"\n".join(incorrect_list)
    write_to_file_in_dir(batch_dir, 'batch_summary', summary)
    print('Done')
    return summary

# rbk_path = r"MachineLearningSummer/rule_book_bank/RAW_RuleBooks_22.txt"
# mapping_path = r"MachineLearningSummer/fallacy_dataset/article_to_label_test.json"
# # dataset_path = r'MachineLearningSummer/fallacy_dataset/30%_of_dataset.csv'
# dataset_path = r'MachineLearningSummer/fallacy_dataset/article_to_label_test.json'
# batch_dir = r"MachineLearningSummer/clean_space/response_bank/batch2"
# batch_classify(rbk_path=rbk_path, dataset_path=dataset_path, mapping_path=mapping_path, batch_dir=dir)