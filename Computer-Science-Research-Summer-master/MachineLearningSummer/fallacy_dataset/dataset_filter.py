from typing import List
import pandas as pd

class DatasetFilter:
    def __init__(self, datasetpath: str) -> None:
        self.dataframe = pd.read_csv(datasetpath)
        self.filtered = None

    def filter(self, columns: List[str]) -> None:
        self.filtered = self.dataframe[columns]
    
    def write_tocsv(self, name, dir="") -> None:
        if dir:
            if dir[-1] == '/':
                self.filtered.to_csv(f'{dir}{name}.csv', header=True, index=False)
            else:
                self.filtered.to_csv(f'{dir}/{name}.csv', header=True, index=False)
        else:
            self.filtered.to_csv(f'{name}.csv', header=True, index=False)