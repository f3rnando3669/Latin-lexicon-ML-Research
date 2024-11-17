import re
from Clients.Utilities.FileUtilities import read_filelines, write_tojson
import json

def extract_tag(tag_pattern, string):
    found = re.search(tag_pattern, string)
    start, end = found.span()
    return string[start:end]

def extract_tags_from(path, identifier_pattern=r'Define <[a-zA-Z]+> to be a defective argument type[\s\S]+', tag_pattern=r'<[a-zA-Z]+>'):
    lines = read_filelines(path)
    tags = []

    for line in lines:
        line.rstrip()
        if re.match(identifier_pattern, line):
            tags.append(extract_tag(tag_pattern, line))
    return tags

# path = r'MachineLearningSummer/rule_book_bank/RAW_RuleBooks_14.txt'
# tag_arr = extract_tags_from(path)
# # print(len(tag_arr))
# path = r'MachineLearningSummer/rule_book_bank/RAW_RuleBooks_12.txt'
# names_arr = extract_tags_from(path, r'[0-9]+\.\s\*\*[\s\S]+\*\*:', r'\*\*[\s\S]+\*\*')
# # print(len(names_arr))
# mapping = {tag:name[2:-2] for tag,name in zip(tag_arr, names_arr)}
# # print(mapping)
# write_tojson(r'MachineLearningSummer/fallacy_dataset/tags.json', mapping)
