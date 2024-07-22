from Clients.Utilities.FileUtilities import read_filelines, write_lines_to_dir, readjson
import re
from extract_rbk_tags import extract_tag

def add_to_rule_book(rulebookpath, match_pattern, string_to_change, replacement, dir, name, mapping_kit=None) -> str:
    lines = read_filelines(rulebookpath)
    new_lines = []

    for line in lines:
        if re.match(match_pattern, line):
            if mapping_kit is not None:
                mapping = mapping_kit[0]
                extract_pattern = mapping_kit[1]
                tag = extract_tag(extract_pattern, line)
                mapped_name = mapping[tag]
                line = re.sub(string_to_change, replacement+mapped_name+' ', line)
            else:
                line = re.sub(string_to_change, replacement, line)
        new_lines.append(line)

    return write_lines_to_dir(dir, name, new_lines)

# mapping_path = r'MachineLearningSummer/fallacy_dataset/tags.json'
# mapping_kit = [readjson(mapping_path), r'<[a-zA-Z]+>']
# path = r'MachineLearningSummer/rulebook_intermediates/rulebk_21_intermediary.txt'
# pattern = r'Define <[a-zA-Z]+> to be a defective argument type [\s\S]+'
# change = r'type '
# repl = r'type called '
# dir = r'MachineLearningSummer/rulebook_intermediates'
# name = 'rbk22'
# add_to_rule_book(path, pattern, change, repl, dir, name, mapping_kit=mapping_kit)

# p = r'[<>a-zA-Z0-9\s]+type[a-zA-Z0-9\s\(\)\.\"\',]+'
# rulebook_path = r'MachineLearningSummer/rule_book_bank/RAW_RuleBooks_18.txt'
# change = r'type '
# repl = r'type usually '
# write_path = r'MachineLearningSummer/rule_book_bank'
# n = 'RAW_RuleBooks'
