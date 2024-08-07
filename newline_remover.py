import os
# a funciton to read through every file in a folder and remove the newline character from the end of each line.
PATH = os.path.dirname(__name__)


def folder_reader(directory):
    for file in os.listdir(os.path.join(PATH, directory)):
        if not file.startswith('.'):
            realFile = directory + "/" + file
            #print("currently working on file {}".format(realFile))
            newline_remover(os.path.join(PATH, realFile))

def newline_remover(file):
    print(file)

    working_file = open(file, "r", encoding='utf-8-sig')
    header = working_file.readline()
    print(header)
    sequence = ""
    for line in working_file:
        sequence += line.replace("\n", '')
    print(sequence)
    return_string = header + sequence
    print(return_string)

    working_file.write(return_string)
    working_file.close()        
    
    print("all newlines removed")

folder_reader('testSequences')