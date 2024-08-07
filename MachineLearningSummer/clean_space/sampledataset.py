import pandas as pd
from dataset_utils import get_labels_and_articles
from random import shuffle

def get_fraction_of_dataset(fraction:float, original_set_path:str, target_dir:str, target_name='') -> None:
    """
    get a randomly sampled fraction of a dataset
    """
    csv_path = original_set_path
    df = pd.read_csv(csv_path)
    df = df.sample(frac=fraction)
    write_dir = target_dir
    if not target_name:
        df.to_csv(write_dir+f'{int(fraction*100)}%_of_dataset.csv', index=False)
    else:
        df.to_csv(write_dir+target_name+'.csv', index=False)

@DeprecationWarning
def partition_dataset(path: str, train_num, test_num: int, shuffle_list=True) -> tuple[dict[str:str]]:
    labels_and_articles = list(get_labels_and_articles(path=path))

    if shuffle_list:
        shuffle(labels_and_articles)

    train_data = {}
    test_data = {}
    test_list = []

    for i, entry in enumerate(labels_and_articles):
        label, article = entry
        if label in train_data:
            if len(train_data[label]) == train_num:
                continue
            labels_and_articles[i] = []
            train_data[label].append(article)
        else:
            labels_and_articles[i] = []
            train_data[label] = [article]

    tracker = {}   
    for entry in labels_and_articles:
        if not entry:
            continue
        label, article = entry
        if label in tracker:
            if tracker[label] == test_num:
                continue
            test_data[article] = label
            test_list.append({'article': article, 'label': label})
            tracker[label] += 1
        else:
            test_data[article] = label
            test_list.append({'article': article, 'label': label})
            tracker[label] = 1
    
    return train_data, test_data, test_list

def get_new_data(path: str, example_count:int, indexes={}, forbidden={}, selected={}):
    """
    get new data from a dataset path\n
    you may specify the indexes to start from per label\n
    you may also specify data that you do not want to be picked\n
    tou may specify the types of labels you want
    """
    if example_count == 0:
        return {}, {}
    labels_and_articles = list(get_labels_and_articles(path=path))

    new_data = {}
    updated = set()
    
    for i, entry in enumerate(labels_and_articles):
        label, article = entry
        if label not in selected:
            continue
        if article in forbidden[label]:
            continue
        if label in indexes:
            if indexes[label] > i:
                continue
        if label in new_data:
            if len(new_data[label]) == example_count:
                if label in updated:
                    continue
                indexes[label] = i
                updated.add(label)
                continue
            new_data[label].append(article)
        else:
            new_data[label] = [article]
    
    return new_data, indexes