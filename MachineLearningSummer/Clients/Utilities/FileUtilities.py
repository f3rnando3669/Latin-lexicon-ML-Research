import datetime
import os
from typing import List
import docx
import csv
import json

def readdocx(docxFile) -> str:
    """
    get a string for a docx file
    """
    doc = docx.Document(docxFile)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

def readfile(path) -> str:
    """
    get a string for a txt file
    """
    fd = open(path)
    text = fd.read()
    fd.close()
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
        dir_size = directory_size(dir)
        fd = open(f"{dir}/{name}_{dir_size}.{type}", "w")
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