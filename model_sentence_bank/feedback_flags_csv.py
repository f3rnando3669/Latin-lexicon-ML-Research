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

        print(art_list)
        print(act_list)
        if len(art_list) > len(act_list):
            extra_classifiers = True

        for i in range(len(act_list)):
            if art_list[i] != act_list[i]:
                error_count += 1

    return error_count, extra_classifiers


def compare_column(file, ai_column, actual_column):
    with open(file, mode='r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            ai_value = row[ai_column]
            actual_value = row[actual_column]

            if ai_value != actual_value:
                print(compare_values(ai_value, actual_value))
            else:
                print("These values are the same!")

csv_file = r'C:\Users\Liam\Desktop\Summer Research\MachineLearningSummer\model_sentence_bank\model_accuracy.csv'
column1 = ' AI Response'
column2 = ' Actual Response'

compare_column(csv_file,column1,column2)