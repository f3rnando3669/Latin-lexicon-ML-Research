import pandas as pd
from collections import OrderedDict
from nltk.corpus import wordnet as wn
from wordnet_refinery import simplify_name


# get the top 100 hypernyms - based on occurrences in wordsandhypernyms.csv
def collect_top_100(frequency_map):
    top100_words = []

    for i, word in enumerate(frequency_map):
        if i == 100:
            break
        top100_words.append(word)

    return top100_words


# create a map of hypernyms and their frequencies
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


# sort the map of hypernyms and frequencies in decreasing order
def sort_frequency_map(frequency_map):
    return OrderedDict(sorted(frequency_map.items(), key=lambda item: item[1], reverse=True))


# recursively find the hypernym hierarchy for a word
def find_root_hypernym(word, collection_of_hypernyms):
    if len(word.hypernyms()) == 0 or simplify_name(word.name()) == "entity":
        return [collection_of_hypernyms]

    hierarchy_of_hypernyms = []
    for hypernym in word.hypernyms():
        hierarchy_of_hypernyms += (find_root_hypernym(hypernym, collection_of_hypernyms + " " + simplify_name(
            hypernym.name())))

    return hierarchy_of_hypernyms


# get all hyponyms for a certain word
def get_hyponyms(word_in):
    word_out = ""

    for hyponym in word_in.hyponyms():
        word_out += simplify_name(hyponym.name()) + " "

    return word_out


# find all senses of a word from the top 100 hypernyms
# look for the hypernym hierarchy and all hyponyms for a certain sense of a word
def divide_words_senses(top100_words):
    set_csv = []
    i = 1
    for simple_word in top100_words:
        for word in wn.synsets(simple_word):
            collection_of_hypernyms = find_root_hypernym(word, "")
            hyponyms = get_hyponyms(word)
            print(collection_of_hypernyms)
            for collection in collection_of_hypernyms:
                hypernyms = "".join(collection)
                if len(hypernyms) > 0:
                    set_csv.append(
                        {"index": i, "word": simplify_name(word.name()), "word_sense": word.name(),
                         "hypernyms": hypernyms[1:], "hyponyms": hyponyms})
                else:
                    set_csv.append(
                        {"index": i, "word": simplify_name(word.name()), "word_sense": word.name(),
                         "hypernyms": " ", "hyponyms": hyponyms})

            i += 1

    return set_csv


# write changes to the top100hypernyms.csv file
def inject(set_csv):
    top100_df = pd.DataFrame.from_dict(set_csv)
    top100_df.to_csv(r'top100hypernyms.csv', index=False, header=True)


df = pd.read_csv("wordsandhypernyms.csv")
saved_column = df["word_hypernym"]

hypernym_frequency_map = sort_frequency_map(get_hypernym_frequency_map(saved_column))
inject(divide_words_senses(collect_top_100(hypernym_frequency_map)))
