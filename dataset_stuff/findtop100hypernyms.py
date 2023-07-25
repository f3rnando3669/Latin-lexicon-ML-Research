import pandas as pd
from collections import OrderedDict
from nltk.corpus import wordnet as wn
from wordnet_refinery import simplify_name

# get the top hypernyms and hyponyms for the top 100 hypernyms


def get_hypernym_frequency_map(categories_list):
    frequency_map = {}

    for hypernym in categories_list:
        if hypernym == " ":
            continue
        if frequency_map.__contains__(hypernym):
            frequency_map[hypernym] += 1
            continue
        frequency_map[hypernym] = 1

    return frequency_map


def sort_frequency_map(frequency_map):
    return OrderedDict(sorted(frequency_map.items(), key=lambda item: item[1], reverse=True))


def get_hypernyms(word_in):
    word_out = ""

    for word in wn.synsets(word_in):
        for hypernym in word.hypernyms():
            word_out += simplify_name(hypernym.name()) + " "

    print(word_out)
    return word_out


def get_hyponyms(word_in):
    word_out = ""

    for word in wn.synsets(word_in):
        for hyponym in word.hyponyms():
            word_out += simplify_name(hyponym.name()) + " "

    print(word_out)
    return word_out


def write_top100(frequency_map):
    set_csv = []

    for i, word in enumerate(frequency_map):
        if i == 100:
            break
        else:
            set_csv.append({"top_words": word, "hypernyms": get_hypernyms(word), "hyponyms": get_hyponyms(word)})

    top100_df = pd.DataFrame.from_dict(set_csv)
    top100_df.to_csv(r'wordsandhypernyms.csv', index=False, header=True)


df = pd.read_csv("wordsandhypernyms.csv")
saved_column = df["word_hypernym"]

hypernym_frequency_map = sort_frequency_map(get_hypernym_frequency_map(saved_column))
write_top100(hypernym_frequency_map)
