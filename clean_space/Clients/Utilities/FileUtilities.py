import datetime
import os
import docx
import csv

def readdocx(docxFile):
    """
    get a string for a docx file
    """
    doc = docx.Document(docxFile)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

def readfile(path):
    """
    get a string for a txt file
    """
    fd = open(path)
    text = fd.read()
    fd.close()
    return text

def readcsv(path):
    fd = open(path, "r")
    read = list(csv.reader(fd))
    fd.close()
    return read

def read_filelines(path):
    """
    get an array where each element is a line of text
    """
    fd = open(path)
    text = fd.readlines()
    fd.close()
    return text

def write_tofile_indir(dir, name, text, type="txt", text_analyzed=""):
    try:
        print("Writing to file")
        current_time = datetime.datetime.now()
        dir_size = directory_size(dir)
        fd = open(f"{dir}/{name}_{dir_size}.{type}", "w")
        fd.write(f"New response iteration made at {current_time}\nFor {text_analyzed}\n" + text + "\n")
        print("Write successful")
        fd.close()
        return 1
    except:
        raise RuntimeError("Could not write to file")

def write_tofile(name, text, type="txt"):
    try:
        print("Writing to file")
        current_time = datetime.datetime.now()
        print(current_time)
        fd = open(f"{name}.{type}", "w")
        print("file created")
        fd.write(f"New response iteration made at {current_time}\n" + text + "\n")
        print("Write successful")
        fd.close()
        return 1
    except:
        raise RuntimeError("Could not write to file")

def directory_size(directory):
    return len(os.listdir(directory)) + 1

def write_tocsv(path, row):
    fd = open(path, "a")
    writer = csv.writer(fd)
    writer.writerow(row)
    fd.close()