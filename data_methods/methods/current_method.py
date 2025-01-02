from collections import Counter

import pandas as pd

from utils.logger import log_execution_time
from utils.tools import create_dataset


# pandarallel.initialize(progress_bar=True)  # Initialize parallelism

def count_past_matches(row: set, combinations: list[set]):
    matches_count_ls = [len(row & sublist) for sublist in combinations]
    matches_count_grp = dict(Counter(matches_count_ls))
    return matches_count_grp


class CurrentMethod:
    def __init__(self, large_size: int = 10000):
        data_size_large = large_size
        data_size_small = 1000
        self.df1 = create_dataset(col_id="A", size=data_size_large)
        self.df2 = create_dataset(col_id="B", size=data_size_small)

    @log_execution_time
    def run_transformation1(self):
        a_array = self.df1.to_numpy()
        b_array = self.df2.to_numpy()
        a_list = [set(a_row) for a_row in a_array]
        b_list = [set(b_row) for b_row in b_array]

        a_match_count = pd.DataFrame({"normal_list_col": a_list}, index=self.df1.index)
        a_match_count["matches_count_dict_col"] = a_match_count["normal_list_col"].map(lambda x: count_past_matches(x, b_list))
        return