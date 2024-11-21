import re
import json

fd = open('existing_defs.txt', 'r')
lines = fd.readlines()
fd.close()

fd = open('abrev_to_fallacy.json', 'r')
mapping = json.load(fd)
fd.close()

rv = ""

for line in lines:
    start = False
    tag = ''
    for char in line:
        if char == '<':
            tag += char
            start = True
        elif start:
            tag += char
        if char == '>':
            break
    if tag in mapping:
        rv += line

fd = open('RAW_Rulebooks_15.txt', 'w')
fd.write(rv)
fd.close()