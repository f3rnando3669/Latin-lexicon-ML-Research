# import docx
import datetime
import os
import re

def readdocx(docxFile):
    """
    get a string for a docx file
    """
    doc = docx.Document(docxFile)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

def readfile(path):
    """
    get a string for a txt file
    """
    fd = open(path)
    text = fd.read()
    fd.close()
    return text

def readfile_lines(path):
    """
    get an array where each element is a line of text
    """
    fd = open(path)
    text = fd.readlines()
    fd.close()
    return text

def get_rule_book(dir, name, type, client, prompts):
    """
    get a string for a rule book\n
    path should point to a txt file
    """
    print("Generating rulebook")
    current_time = datetime.datetime.now()
    dir_size = directory_size(dir)
    fd_raw_rulebk = open(f"{dir}{name}_{dir_size}.{type}", "w")
    fd_raw_rulebk.write(f"New Rule book iteration made at {current_time}\n" + client.generate_using_prompts(prompts=prompts) + "\n")
    print("Rulebook appended to file successfully")
    # text = fd_raw_rulebk.read()
    fd_raw_rulebk.close()
    return f"{dir}{name}_{dir_size}.{type}"

def write_to_file_in_dir(dir, name, text, type="txt", text_analyzed=""):
    try:
        print("Writing to file")
        current_time = datetime.datetime.now()
        dir_size = directory_size(dir)
        fd = open(f"{dir}/{name}_{dir_size}.{type}", "w")
        fd.write(f"New response iteration made at {current_time}\nFor {text_analyzed}\n" + text + "\n")
        print("Write successful")
        fd.close()
        return 1
    except:
        RuntimeError("Could not write to file")

def write_to_file(name, text, type="txt"):
    try:
        print("Writing to file")
        current_time = datetime.datetime.now()
        fd = open(f"{name}.{type}", "w")
        fd.write(f"New response iteration made at {current_time}\n" + text + "\n")
        print("Write successful")
        fd.close()
        return 1
    except:
        RuntimeError("Could not write to file")

def directory_size(directory):
    return len(os.listdir(directory)) + 1

def analyze_with_rulebook(client, prompts, text_dir, rulebook_path, find=[]):
        print("starting analyzing")
        rule_book = readfile(rulebook_path)
        for path in os.listdir(text_dir):
            if path not in find:
                client.clear()
                prompts.clear()
                file_path = text_dir + path
                speech = readfile(file_path)
                print(path)
                prompts.add_var_prompt("<RB>", rule_book)
                prompts.add_var_prompt("<SP>", speech)
                # # # prompts.add_rhetoric_prompt("<SP>", "<RB>")
                # # # prompts.add_argument_prompt("<SP>", "<RB>")
                prompts.add_rating_prompt("<SP>", "<RB>")

                response = client.generate_using_prompts(prompts=prompts)
                # print(f"Response:\n{response}")
                write_to_file_in_dir("/home/andi/summer2024/MachineLearningSummer/response_bank", "response", response, "txt", path)
        print("done with analysis")

def remove_headings(arr):
    """
    takes an array of sentences
    produces an array that omits headings
    """
    rv = []
    for line in arr:
        line = re.sub(r"[0-9]. \*\*([a-zA-Z]* [a-zA-Z]*)*\*\*:", "", line)
        if line:
            rv.append(line)
    
    return rv

def remove_tab_spacing(arr):
    """
    takes an array of sentences
    produces an array that has sentences reformatted to have no tab indentation
    """
    rv = []
    for line in arr:
        line = re.sub(r"(\s{3})- \*\*([a-zA-Z]*)*\*\*", r"\1", line)
        if line:
            rv.append(line)
    
    return rv

# lines = readfile_lines("/home/andi/summer2024/MachineLearningSummer/rule_book_bank/RAW_RuleBooks_9.txt")
# headingless = remove_headings(lines)
# # print(headingless)
# stuff = "".join(headingless)
# _dir = "/home/andi/summer2024/MachineLearningSummer/rule_book_bank"
# write_to_file_in_dir(_dir,"RAW_RuleBooks", stuff)
line = "   - **Inappropriate Reason**:"
print(remove_tab_spacing([line]))