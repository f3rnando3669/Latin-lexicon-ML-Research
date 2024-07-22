import datetime
import os
from typing import List
import csv
import json
import re

def readfile(path) -> str:
    """
    get a string for a txt file
    """
    with open(path, 'r', encoding='utf-8') as fd:
        text = fd.read()
    return text

def readcsv(path) -> List[str]:
    """
    read a csv file
    """
    fd = open(path, "r")
    read = list(csv.reader(fd))
    fd.close()
    return read

def read_filelines(path) -> List[str]:
    """
    get an array where each element is a line of text
    """
    fd = open(path)
    text = fd.readlines()
    fd.close()
    return text

def readjson(path):
    """
    read a json file\n
    returns a json object
    """
    fd = open(path, "r")
    jsonobject = json.load(fd)
    fd.close()
    return jsonobject

def write_to_file_in_dir(dir, name, text, type="txt", text_analyzed="") -> None:
    """
    write to a file in a directory
    """
    try:
        print("Writing to file")
        current_time = datetime.datetime.now()
        directory_list = os.listdir(dir) 
        count = 1
        for item in directory_list:
            if re.match(f'{name}_'+r'[0-9]+'+f'.{type}', item):
                count += 1
        fd = open(f"{dir}/{name}_{count}.{type}", "w")
        fd.write(f"New response iteration made at {current_time}\nFor {text_analyzed}\n" + text + "\n")
        print("Write successful")
        fd.close()
    except:
        raise RuntimeError("Could not write to file")

def write_to_file(name, text, type="txt") -> None:
    """
    write to a file
    """
    try:
        print("Writing to file")
        current_time = datetime.datetime.now()
        print(current_time)
        fd = open(f"{name}.{type}", "w")
        print("file created")
        fd.write(f"New response iteration made at {current_time}\n" + text + "\n")
        print("Write successful")
        fd.close()
    except:
        raise RuntimeError("Could not write to file")

def directory_size(directory) -> int:
    """
    find out the size of a directory
    """
    return len(os.listdir(directory)) + 1

def write_tocsv(path, row) -> None:
    """
    write to a csv file\n
    Would append new row to the file if data already exists in the file
    """
    try:
        fd = open(path, "a")
        writer = csv.writer(fd)
        writer.writerow(row)
        fd.close()
    except:
        raise RuntimeError("Could not write to csv file")

def write_tojson(path, data) -> None:
    """
    Write to a json file\n
    Would override file if data already exists in the file
    """
    try:
        fd = open(path, "w")
        json.dump(data, fd)
        fd.close()
    except:
        raise RuntimeError("Could not write to json file")
    
def write_lines(path, lines) -> None:
    try:
        fd = open(path, 'w')
        fd.writelines(lines)
        fd.close()
    except:
        raise RuntimeError("Could not write to txt file")

def write_lines_to_dir(dir, name, lines, type="txt") -> str:
    try:
        # print("Writing to file")
        directory_list = os.listdir(dir) 
        count = 1
        for item in directory_list:
            if re.match(f'{name}_'+r'[0-9]+'+f'.{type}', item):
                count += 1
        path = ''
        if dir[-1] != '/':
            path = f"{dir}/{name}_{count}.{type}"
        else:
            path = f"{dir}{name}_{count}.{type}"
        fd = open(path, "w")
        fd.writelines(lines)
        # print("Write successful")
        fd.close()
        return path
    except:
        raise RuntimeError("Could not write to file")
