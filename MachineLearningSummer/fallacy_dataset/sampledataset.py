import pandas as pd

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