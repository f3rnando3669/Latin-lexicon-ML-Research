# import re
# import pandas as pd
#
# import spacy
#
# fd = open("C:/Users/Andi/PycharmProjects/researchstuff2023/Computer-Science-Research-Summer/CoreNLP/NLP_Software/src"
#           "/main/java/NLP/Software/Pipeline/output.txt", "r")
# fd_list = fd.readlines()
#
# table = []
#
# for i in range(6, len(fd_list), 6):
#     original_input = fd_list[i - 6].rstrip("\n").split(":")
#     post_lemma = fd_list[i - 5].rstrip("\n").split(":")
#     post_pos = fd_list[i - 4].rstrip("\n").split(":")
#     pattern_matching = fd_list[i - 3].rstrip("\n").split(":")
#     pattern_matched_found = fd_list[i - 2].rstrip("\n").split(":")
#     # new_line = fd_list[i].rstrip("\n")
#
#     if re.match(" Pattern not found", pattern_matching[1]):
#         table.append({original_input[0]: original_input[1][1:-1], post_lemma[0]: post_lemma[1][1:-2],
#                       post_pos[0]: post_pos[1][1:-2],
#                       pattern_matching[0]: pattern_matching[1][1:], pattern_matched_found[0]: "N/A"})
#         continue
#
#     table.append(
#         {original_input[0]: original_input[1][1:-1], post_lemma[0]: post_lemma[1][1:-2], post_pos[0]: post_pos[1][1:-2],
#          pattern_matching[0]: pattern_matching[1][1:], pattern_matched_found[0]: pattern_matching[2][1:]})
#
# df = pd.DataFrame.from_dict(table)
# df.to_csv("data_organised_from_output.txt", index=False, header=True)

import sys

import spacy
from nltk import Tree

en_nlp = spacy.load("en_core_web_sm")


def file_processing(fd):
    fd_list = fd.readlines()

    table = []

    for i in range(3, len(fd_list), 4):
        original_input = fd_list[i - 3].rstrip("\n").split(":")
        matched_words = fd_list[i - 2].rstrip("\n").split(":")
        object_of_sentence = fd_list[i - 1].rstrip("\n").split(":")

        # print(original_input)
        # print(matched_words)
        # print(object_of_sentence)

        table.append(
            {original_input[0]: original_input[1], matched_words[0]: matched_words[1],
             object_of_sentence[0]: object_of_sentence[1]})

    return table


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


file_in = open("C:/Users/Andi/PycharmProjects/researchstuff2023/Computer-Science-Research-Summer/CoreNLP/NLP_Software"
               "/src/main/java/NLP/Software/Pipeline/output.txt", "r")
table = file_processing(file_in)
file_in.close()

file_out = open("C:/Users/Andi/PycharmProjects/researchstuff2023/Computer-Science-Research-Summer/CoreNLP"
                "/NLP_Software/src/main/python/dependencytrees.txt", "a+")

sys.stdout = file_out

file_out.seek(0)

previous_text = file_out.read()

print(previous_text)

for item in table:
    original_in = en_nlp(item["Original Input"])

    for sent in original_in.sents:
        to_nltk_tree(sent.root).pretty_print()
