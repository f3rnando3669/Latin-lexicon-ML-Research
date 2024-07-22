import re
from Utilities.FileUtilities import read_filelines, write_lines


def remove_rulebook_examples(rulebookpath, targetpath, match_pattern=r'^[<>a-zA-Z\s,\'\"\.]+\(e\.g\.,', sub_pattern=r'(^[<>a-zA-Z\s,\'\"\.]+\(e\.g\.)([\s\S]+)$') -> None:
    rbk_path = rulebookpath
    lines = read_filelines(rbk_path)

    new_lines = []
    for line in lines:
        line = line.rstrip()
        if re.match(match_pattern, line):
            line = re.sub(sub_pattern, r'\1', line)
        new_lines.append(line+'\n')

    write_lines(targetpath, new_lines)