from prompt_client import Client
from prompt_list import PromptList
from utilities import readfile, analyze_with_rulebook, write_to_file_in_dir, get_rule_book, r_enforce_prompt, remove_headings, remove_indent_spacing, remove_line_spacing, fit_to_template
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

    # create rulebook
    # rhetorica_path = r"/home/andi/summer2024/MachineLearningSummer/rhetoradher_bks1and2.txt"
    # rhetorica = readfile(rhetorica_path)
    # prompts.add_var_prompt("<RH>", rhetorica)
    rulebook_dir = r"/home/andi/summer2024/MachineLearningSummer/rule_book_bank"
    # prompts.add_rulebook_prompt("<RH>")
    # # rulebook_path = get_rule_book(rulebook_dir, "RAW_RuleBooks", "txt", client=client, prompts=prompts)
    # # rulebook = readfile(rulebook_path)
    # rulebook = client.generate_using_prompts(prompts=prompts)
    # write_to_file_in_dir(rulebook_dir, "RAW_RuleBooks", rulebook, text_analyzed="Rhetorica Rulebook")
    # go thru rulebook, check for stuff that lack examples
    rulebook = readfile(r"/home/andi/summer2024/MachineLearningSummer/rule_book_bank/RAW_RuleBooks_11.txt")
    rulebook_arr = rulebook.split("\n")
    # rulebook_arr  = remove_headings(rulebook_arr)
    # rulebook_arr = remove_indent_spacing(rulebook_arr)
    rulebook_arr = fit_to_template(3, rulebook_arr, 5)
    rulebook = "".join(rulebook_arr)
    write_to_file_in_dir(rulebook_dir, "RAW_RuleBooks", rulebook, text_analyzed="Rhetorica Rulebook")
    # rulebook, enforce = r_enforce_prompt(rulebook)
    # if enforce:
    #     client.clear()
    #     prompts.clear()
    #     prompts.add_prompt(rulebook)
    #     rulebook = client.generate_using_prompts(prompts=prompts)
    # write_to_file_in_dir(rulebook_dir, "RAW_RuleBooks", rulebook, text_analyzed="Rhetorica Rulebook")
    # if any lack examples make gpt fill them out using multi-shot prompting
    # return a final rulebook

    # rulebook_path = "/home/ml/MLResearch2024/MachineLearningSummer/rule_book_bank/RAW_RuleBooks_10.txt"
    # speech_path = "/home/ml/MLResearch2024/MachineLearningSummer/Speeches/Rule Book 9 Test"
    # analyze_with_rulebook(client=client, prompts=prompts, rulebook_path=rulebook_path, text_dir=speech_path)
    
    # symbol_list = readfile("/home/ml/MLResearch2024/MachineLearningSummer/model_sentence_bank/comprehensive_symbol_system.txt")
    # model1 = readfile("/home/ml/MLResearch2024/MachineLearningSummer/model_sentence_bank/model1.txt")
    # model1_analysis = readfile("/home/ml/MLResearch2024/MachineLearningSummer/model_sentence_bank/model1_analysis.txt")
    # model2 = readfile("/home/ml/MLResearch2024/MachineLearningSummer/model_sentence_bank/model4.txt")

    # prompts.add_var_prompt("Symbols",symbol_list)
    # prompts.add_symbol_prompt_one_shot(model1, model1_analysis,model2)
    # write_to_file_in_dir("/home/ml/MLResearch2024/MachineLearningSummer/response_bank", "response",client.generate_using_prompts(prompts=prompts))