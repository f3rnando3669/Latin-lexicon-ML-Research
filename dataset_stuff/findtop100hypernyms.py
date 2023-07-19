import pandas as pd


def get_hypernym_frequency_map(categories_list):
    frequency_map = {}

    for i, hypernym in enumerate(categories_list):
        if frequency_map.__contains__(categories_list[i]):
            frequency_map[categories_list[i]] += 1
            continue
        frequency_map[categories_list[i]] = 0

    return frequency_map


def sort_frequency_map(frequency_map):
    return dict(sorted(frequency_map.items(), key=lambda item: item[1], reverse=True))


def write_top100(frequency_map):
    title = ["top_words"]
    set_csv = []

    for i, word in enumerate(frequency_map):
        if i == 100:
            break
        else:
            set_csv.append({"top_words": word})

    top100_df = pd.DataFrame.from_dict(set_csv)
    top100_df.to_csv(r'top100hypernyms.csv', index=False, header=True)


df = pd.read_csv("wordsandhypernyms.csv")
saved_column = df["categories"]

hypernym_frequency_map = get_hypernym_frequency_map(saved_column)
write_top100(hypernym_frequency_map)
