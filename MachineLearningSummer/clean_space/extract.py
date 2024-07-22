from typing import List
from Clients.Utilities.FileUtilities import read_filelines, readjson
import re

mapping_path = r"MachineLearningSummer/fallacy_dataset/abrev_to_fallacy.json"
label_to_article_map = readjson(mapping_path)

def extract_result(path: str) -> bool:
    """
    check for the label specified by GPT as correct
    """
    lines = read_filelines(path)[::-1]
    for line in lines:
        rv = ''
        rv_b = ''
        accum = False
        accum_b = False
        
        line = "".join(line.split(" ")[::-1])
        for char in line:
            if char == '<':
                accum = True
                rv = '<'
            elif accum:
                rv += char
            if char == '>':
                if rv in label_to_article_map:
                    return rv
                accum = False
                rv = ''

            if char == '(':
                accum_b = True
                rv_b = '<'
            elif accum_b:
                rv_b += char
            if char == ')':
                rv_b = rv_b[:-1]+'>'
                if rv_b in label_to_article_map:
                    return rv_b
                accum_b = False
                rv_b = ''

def iscorrect(path: str):
    """
    check if the label from gpt matches the filename
    """
    file = path.split('/')[-1]
    filename, suffix = file.split('_')
    filename = '<'+filename+'>'
    propername = filename+'_'+suffix
    if re.match(r'\<[A-Z]+\>_[0-9]+.txt', propername):
        extracted = extract_result(path)
        return extracted == filename
    else:
        return False
