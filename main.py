from prompt_client import Client
from prompt_list import PromptList
from utilities import readfile, readdocx, get_rule_book, write_to_file, write_to_file_in_dir
import os
if __name__ == "__main__":
    print("===START===")
    # rhetorica = readfile(r"/home/ml/MLResearch2024/rhetoradher_bks1and2.txt")
    # rhetorica_summary = readdocx(r"/home/ml/MLResearch2024/Notes on Rhetorica ad Her.docx")
    
    # rhetorica_prompt = "Let the following text be <RH>, by Cicero. Give a detailed outline and rule-book for excellent rhetoric according to <RH>: <RH>\n" + rhetorica
    # prompts.add_rulebook_prompt(rhetorica) # hover over the function
    # print(prompts)
    # prompts.add_prompt([rhetorica_prompt, 0])
    # prompts.add_prompt(["Give a summary and rule-book for defective arguments according to <RH>", 0])
    # rule_path = get_rule_book("/home/ml/MLResearch2024/rule_book_bank/", "RAW_RuleBooks", "txt", client, prompts)
    # rule_book = readfile(rule_path)
    client = Client()
    prompts = PromptList()
    

    model1 = readfile("/home/ml/MLResearch2024/MachineLearningSummer/model_sentence_bank/model1.txt")
    model1_analysis = readfile("/home/ml/MLResearch2024/MachineLearningSummer/model_sentence_bank/model1_analysis.txt")
    model2 = readfile("/home/ml/MLResearch2024/MachineLearningSummer/model_sentence_bank/model2.txt")