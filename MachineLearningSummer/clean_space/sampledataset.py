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

# original_set_path=r'MachineLearningSummer/fallacy_dataset/datasets/80%_of_70%_of_dataset.csv'
# target_dir = r'MachineLearningSummer/fallacy_dataset/datasets/'
# target_name = r'30%_of_80%_of_70%_of_dataset'
# get_fraction_of_dataset(fraction=0.3, original_set_path=original_set_path, target_dir=target_dir, target_name=target_name)

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

def get_training_data(path, train_num, indexes, forbidden, selected):
    if train_num == 0:
        return {}, {}
    labels_and_articles = list(get_labels_and_articles(path=path))

    train_data = {}
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
        if label in train_data:
            if len(train_data[label]) == train_num:
                if label in updated:
                    continue
                indexes[label] = i
                updated.add(label)
                continue
            train_data[label].append(article)
        else:
            train_data[label] = [article]
    
    return train_data, indexes

def get_test_data(path, test_num, indexes, forbidden):
    if test_num == 0:
        return {}, {}
    labels_and_articles = list(get_labels_and_articles(path=path))

    test_data = {}
    updated = set()
    
    for i, entry in enumerate(labels_and_articles):
        label, article = entry
        if article in forbidden[label]:
            continue
        if label in indexes:
            if indexes[label] > i:
                continue
        if label in test_data:
            if len(test_data[label]) == test_num:
                if label in updated:
                    continue
                indexes[label] = i
                updated.add(label)
                continue
            test_data[label].append(article)
        else:
            test_data[label] = [article]
    
    return test_data, indexes