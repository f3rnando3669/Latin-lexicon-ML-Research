from Clients.Utilities.FileUtilities import read_filelines, write_lines_to_dir
import re

def add_to_rule_book(rulebookpath, match_pattern, string_to_change, replacement, dir, name):
    lines = read_filelines(rulebookpath)
    new_lines = []

    for line in lines:
        if re.match(match_pattern, line):
            line = re.sub(string_to_change, replacement, line)
        new_lines.append(line)

    write_lines_to_dir(dir, name, new_lines)

# p = r'[<>a-zA-Z0-9\s]+type[a-zA-Z0-9\s\(\)\.\"\',]+'
# rulebook_path = r'MachineLearningSummer/rule_book_bank/RAW_RuleBooks_18.txt'
# change = r'type '
# repl = r'type usually '
# write_path = r'MachineLearningSummer/rule_book_bank'
# n = 'RAW_RuleBooks'
