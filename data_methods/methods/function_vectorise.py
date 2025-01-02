from collections import Counter

import numpy as np
from pandarallel import pandarallel
import pandas as pd
from numba import jit, njit, int64, int32
from numba.typed import Dict, List
import numba

from utils.logger import log_execution_time
from utils.tools import create_dataset

# pandarallel.initialize(progress_bar=True)  # Initialize parallelism




class VectoriseFunction:
    def __init__(self, large_size: int =10000):
        data_size_large = large_size
        data_size_small = 1000
        self.df1 = create_dataset(col_id="A", size=data_size_large)
        self.df2 = create_dataset(col_id="B", size=data_size_small)

    def count_past_matches(self, row: set):
        matches_count_ls = [len(row & sublist) for sublist in self.combinations]
        matches_count_grp = dict(Counter(matches_count_ls))
        return matches_count_grp
    @log_execution_time
    def run_transformation1(self):
        a_array = self.df1.to_numpy()
        b_array = self.df2.to_numpy()
        a_list = [set(a_row) for a_row in a_array]
        self.combinations = [set(b_row) for b_row in b_array]

        a_match_count = pd.DataFrame({"normal_list_col": a_list}, index=self.df1.index)

        a_match_count['result'] = np.vectorize(self.count_past_matches)(a_match_count['normal_list_col'].to_numpy())

        # vectorized_function = np.vectorize(count_past_matches, excluded=['combinations'])
        # a_match_count['result'] = vectorized_function(a_match_count['normal_list_col'].to_numpy(), combinations)
        return