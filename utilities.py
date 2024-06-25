# import docx
import datetime
import os
import re
from typing import List

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
    new_rule_path = ""
    if dir[-1] == "/":
        new_rule_path = f"{dir}{name}_{dir_size}.{type}"
    else:
        new_rule_path = f"{dir}/{name}_{dir_size}.{type}"
    fd_raw_rulebk = open(new_rule_path, "w")
    fd_raw_rulebk.write(f"New Rule book iteration made at {current_time}\n" + client.generate_using_prompts(prompts=prompts) + "\n")
    print("Rulebook appended to file successfully")
    # text = fd_raw_rulebk.read()
    fd_raw_rulebk.close()
    return new_rule_path

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
        print(current_time)
        fd = open(f"{name}.{type}", "w")
        print("file created")
        fd.write(f"New response iteration made at {current_time}\n" + text + "\n")
        print("Write successful")
        fd.close()
        return 1
    except:
        RuntimeError("Could not write to file")

def directory_size(directory):
    return len(os.listdir(directory)) + 1

def analyze_with_rulebook(client, prompts, text_dir, rulebook_path, find=[]):
        # should probably be moved to the client
        # seems like a client function
        # I'll do this in my free time
        print("starting analyzing")
        rule_book = readfile(rulebook_path)
        for path in os.listdir(text_dir):
            if path not in find:
                client.clear()
                prompts.clear()
                if text_dir[-1] != "/":
                    file_path = f"{text_dir}/{path}"
                speech = readfile(file_path)
                print(path)
                prompts.add_var_prompt("<RB>", rule_book)
                prompts.add_var_prompt("<SP>", speech)
                prompts.add_rating_prompt("<SP>", "<RB>")

                response = client.generate_using_prompts(prompts=prompts)
                write_to_file_in_dir("/home/ml/MLResearch2024/MachineLearningSummer/response_bank", "response", response, "txt", path)
                
        print("done with analysis")

def autocomplete(client, prompts, text_path):
    content = readfile(text_path)
    prompts.add_prompt(content)
    print("starting auto completion")
    response = client.generate_using_prompts(prompts)
    print("auto completion successful")
    prompts.clear()
    return response

def remove_headings(arr: List[str]) -> List[str]:
    """
    takes an array of sentences
    produces an array that omits headings
    """
    rv = []
    for line in arr:
        line = re.sub(r"[0-9]. \*\*([a-zA-Z]* [a-zA-Z]*)*\*\*:", r"", line)
        if line:
            rv.append(line)
    
    return rv

def remove_indent_spacing(arr: List[str]) -> List[str]:
    """
    takes an array of sentences
    produces an array that has sentences reformatted to have no tab indentation
    """
    rv = []
    for line in arr:
        line = line.strip()
        if line:
            rv.append(line + "\n")
    
    return rv

def remove_line_spacing(text: str) -> str:

    rv = ""
    window_length = 0

    for i in range(len(text)):
        if text[i] != '\n':
            if window_length > 0:
                rv += "\n"
                window_length = 0
            rv += text[i]
        else:
            window_length += 1
    
    return rv

def r_enforce_prompt(text, starts_with, prompt_tail, delimiter="\n", start=0, end=0):
    if end == 0:
        end = len(text)
    lines = text.split(delimiter)
    unrelated = []
    complete = []
    incomplete = []
    enforce = False
    # print(lines)
    for i, line in enumerate(lines):
        if i < start:
            continue
        if i > end:
            break
        line = line.strip()
        if line.startswith(starts_with):
            if line:
                # print(line)
                line_arr = line.split(" ")

                if f"{prompt_tail}" in line_arr:
                    complete.append(line+"\n")
                else:
                    incomplete.append(line + f",{prompt_tail}\n")
                    # print(line_arr)
                    if not enforce:
                        enforce = True
        else:
            unrelated.append(line)

    return "".join(complete+incomplete).rstrip(), enforce

def get_start(text, prefix_pattern=r"- "):
    prefix = re.sub(prefix_pattern, r"\1", text)
    return prefix

def get_shot_prompt(path, starts_with, prompt_tail, start=0, end=0):
    text = readfile(path)
    prompt, _ = r_enforce_prompt(text, starts_with=starts_with, prompt_tail=prompt_tail, start=start, end=end)
    return prompt

