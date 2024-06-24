import os
import csv
import re

def compare_values(ai, actual):
    expression = r'\((.+)\)'
    match1 = re.search(expression, ai)
    match2 = re.search(expression, actual)
    error_count = 0
    extra_classifiers = False

    if match1 and match2:
        artifical = match1.group(1)
        act = match2.group(1)

        art_list = artifical.split('-')
        act_list = act.split('-')

        print(act_list)
        print(art_list)


def compare_column(file, ai_column, actual_column):
    with open(file, mode='r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            ai_value = row[ai_column]
            actual_value = row[actual_column]
            print(compare_values(ai_value, actual_value))

csv_file = r'C:\Users\Liam\Desktop\Summer Research\MachineLearningSummer\model_sentence_bank\model_accuracy.csv'
column1 = ' AI Response'
column2 = ' Actual Response'

compare_column(csv_file,column1,column2)