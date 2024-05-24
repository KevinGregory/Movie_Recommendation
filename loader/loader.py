import pandas as pd
import numpy as np

from params.constants import DatasetName, DATASET_PATHS

import pandas as pd
from params.constants import DatasetName, DATASET_PATHS

class DataLoader:
    def __init__(self, dataset_name, batch_size=1, shuffle=False):
        self.dataset_name = dataset_name
        self.batch_size = batch_size
        self.shuffle = shuffle

        # Ensure the dataset_name is a valid DatasetName enum member
        if dataset_name in DatasetName.__members__:
            dataset_enum = DatasetName[dataset_name]
            self.data = pd.read_csv(DATASET_PATHS[dataset_enum]).astype(str)
            
        else:
            raise ValueError(f"{dataset_name} is not a valid dataset name")

    def __iter__(self):
        self.n = 0
        if self.shuffle:
            self.data = self.data.sample(frac=1).reset_index(drop=True)
        return self

    def __next__(self):
        if self.n < len(self.data):
            batch = self.data.iloc[self.n:self.n+self.batch_size]
            self.n += self.batch_size
            return batch
        else:
            raise StopIteration


# Example usage:
# dataloader = CSVDataLoader('path_to_csv.csv', batch_size=10, shuffle=True)
# for batch in dataloader:
#     print(batch)
