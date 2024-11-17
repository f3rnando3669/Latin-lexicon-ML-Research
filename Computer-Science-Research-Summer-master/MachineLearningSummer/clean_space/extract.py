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
        line = line.rstrip()
        line_arr = " ".join(line.split(" ")[::-1]).split(" ")
        for word in line_arr:
            result = re.search(r'(<[\S]+>)|(\([\S]+\))', word)
            if result:
                tag = result.group()
                
                for i in range(len(tag)):
                    tag = tag.rstrip('>')
                    tag = tag.strip('<')
                    tag = tag.rstrip(')')
                    tag = tag.strip('(')
                tag = '<'+tag+'>'
                if tag in label_to_article_map:
                    # print(tag, "TAG")
                    return tag
    
        result = re.search(r'\\langle [a-zA-Z]+ \\rangle', line)
        if result:
            tag = result.group()
            tag = re.sub(r'\\langle', '', tag)
            tag = re.sub(r'\\rangle', '', tag)
            for i in range(len(tag)):
                tag = tag.rstrip('>')
                tag = tag.strip('<')
                tag = tag.rstrip(')')
                tag = tag.strip('(')
                tag = tag.rstrip('}')
                tag = tag.strip('{')
                tag = tag.rstrip(' ')
                tag = tag.strip(' ')
            tag = '<'+tag+'>'
            if tag in label_to_article_map:
                return tag

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

def iscorrect_text(correct_tag: str, text: str) -> bool:
    """
    check if the label from gpt matches the expected tag
    """
    extracted = extract_result_from_text(text)
    # print(correct_tag, extracted)
    return correct_tag == extracted


def extract_result_from_text(text: str) -> str:
    """
    check for the label specified by GPT as correct
    """
    lines = text.split('\n')[::-1]
    for line in lines:
        line = line.rstrip()
        line_arr = " ".join(line.split(" ")[::-1]).split(" ")
        for word in line_arr:
            result = re.search(r'(<[\S]+>)|(\([\S]+\))', word)
            if result:
                tag = result.group()
                
                for i in range(len(tag)):
                    tag = tag.rstrip('>')
                    tag = tag.strip('<')
                    tag = tag.rstrip(')')
                    tag = tag.strip('(')
                tag = '<'+tag+'>'
                if tag in label_to_article_map:
                    # print(tag, "TAG")
                    return tag
    
        result = re.search(r'\\langle [a-zA-Z]+ \\rangle', line)
        if result:
            tag = result.group()
            tag = re.sub(r'\\langle', '', tag)
            tag = re.sub(r'\\rangle', '', tag)
            for i in range(len(tag)):
                tag = tag.rstrip('>')
                tag = tag.strip('<')
                tag = tag.rstrip(')')
                tag = tag.strip('(')
                tag = tag.rstrip('}')
                tag = tag.strip('{')
                tag = tag.rstrip(' ')
                tag = tag.strip(' ')
            tag = '<'+tag+'>'
            if tag in label_to_article_map:
                # print(tag, "TAG")
                return tag
