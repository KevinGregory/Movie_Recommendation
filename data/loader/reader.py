import pandas as pd
import numpy as np

import schema.constants as C

def data_reader(dataset: C.DATASETS):
    return pd.read_csv(f"{C.base_path}/{dataset.value}.csv")