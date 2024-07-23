import pandas as pd
from dataset_utils import get_labels_and_articles

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

def partition_dataset(path: str, num: int) -> tuple[dict[str:str]]:
    labels_and_articles = get_labels_and_articles(path=path)
    train_data = {}
    test_data = {}

    for label, article in labels_and_articles:
        if label in train_data:
            if len(train_data[label]) == num:
                test_data[article] = label
                continue
            train_data[label].append(article)
        else:
            train_data[label] = [article]
    
    return train_data, test_data
