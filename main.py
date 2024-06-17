from prompt_client import Client
from prompt_list import PromptList
from utilities import get_file_string, readdocx, get_rule_book, write_to_file, write_to_file_in_dir
import os
if __name__ == "__main__":
    print("===START===")
    # rhetorica = get_file_string(r"/home/ml/MLResearch2024/rhetoradher_bks1and2.txt")
    # rhetorica_summary = readdocx(r"/home/ml/MLResearch2024/Notes on Rhetorica ad Her.docx")
    
    # rhetorica_prompt = "Let the following text be <RH>, by Cicero. Give a detailed outline and rule-book for excellent rhetoric according to <RH>: <RH>\n" + rhetorica
    # prompts.add_rulebook_prompt(rhetorica) # hover over the function
    # print(prompts)
    # prompts.add_prompt([rhetorica_prompt, 0])
    # prompts.add_prompt(["Give a summary and rule-book for defective arguments according to <RH>", 0])
    # rule_path = get_rule_book("/home/ml/MLResearch2024/rule_book_bank/", "RAW_RuleBooks", "txt", client, prompts)
    # rule_book = get_file_string(rule_path)
    client = Client()
    prompts = PromptList()
    rule_book = get_file_string(r"/home/ml/MLResearch2024/rule_book_bank/RAW_RuleBooks_9.txt")

    for path in os.listdir("/home/ml/MLResearch2024/Speeches/Rule Book 9 Test"):
        client.clear()
        prompts.clear()
        file_path = "/home/ml/MLResearch2024/Speeches/Rule Book 9 Test/" + path
        speech = get_file_string(file_path)
        print(path)
        prompts.add_var_prompt("<RB>", rule_book)
        prompts.add_var_prompt("<SP>", speech)
        # # # prompts.add_rhetoric_prompt("<SP>", "<RB>")
        # # # prompts.add_argument_prompt("<SP>", "<RB>")
        prompts.add_rating_prompt("<SP>", "<RB>")

        response = client.generate_using_prompts(prompts=prompts)
        write_to_file_in_dir("/home/ml/MLResearch2024/response_bank/", "response", response, "txt", path)