import numpy as np
import pandas as pd

def create_dataset(col_id: str, size: int = 10000):
    data = pd.DataFrame({
        f'{col_id}1': np.random.randint(1, 7, size=size),
        f'{col_id}2': np.random.randint(1, 7, size=size),
        f'{col_id}3': np.random.randint(1, 7, size=size),
        f'{col_id}4': np.random.randint(1, 7, size=size),
        f'{col_id}5': np.random.randint(1, 7, size=size),
        f'{col_id}6': np.random.randint(1, 7, size=size),
    })
    return data