from Clients.Utilities.FileUtilities import read_filelines, readjson
import re

mapping_path = r"Computer-Science-Research-Summer/MachineLearningSummer/fallacy_dataset/abrev_to_fallacy.json"
label_to_article_map = readjson(mapping_path)

def extract_result(path) -> None:
    lines = read_filelines(path)[::-1]
    for line in lines:
        rv = ''
        accum = False
        line = "".join(line.split(" ")[::-1])
        for char in line:
            if char == '<':
                accum = True
                rv = '<'
            elif accum:
                rv += char
            if char == '>':
                if rv in label_to_article_map:
                    # print(rv)
                    return rv
                accum = False
                rv = ''

def iscorrect(path):
    file = path.split('/')[-1]
    filename, suffix = file.split('_')
    filename = '<'+filename+'>'
    propername = filename+'_'+suffix
    if re.match(r'\<[A-Z]+\>_[0-9]+.txt', propername):
        extracted = extract_result(path)
        return extracted == filename, 1
    else:
        return False, 0
