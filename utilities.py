import docx
import datetime
import os

def readdocx(docxFile):
    """
    get a string for a docx file
    """
    doc = docx.Document(docxFile)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

def get_file_string(path):
    """
    get a string for a txt file
    """
    fd = open(path)
    text = fd.read()
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