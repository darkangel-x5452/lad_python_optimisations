from collections import Counter

import numpy as np
from numba.typed import Dict

from utils.logger import log_execution_time
from utils.tools import create_dataset

# def count_past_matches(row: set, combinations: list[set]):
#     matches_count_ls = [len(row & sublist) for sublist in combinations]
#     matches_count_grp = dict(Counter(matches_count_ls))
#     return matches_count_grp


class JitCompile:
    def __init__(self):
        data_size_large = 1000000
        data_size_small = 1000
        self.df1 = create_dataset(col_id="A", size=data_size_large)
        self.df2 = create_dataset(col_id="B", size=data_size_small)

    @log_execution_time
    def run_transformation1(self):
        df1_array = self.df1.to_numpy()
        df2_array = self.df2.to_numpy()
        np_array_list = [(row == df1_array) for row in df2_array]
        # TODO: cannot do numpy sum for each list element due to bool type.
        ## Converting bool type causes memory error
        array_count_ls = []
        for _row in np_array_list:
            object_array = np.array(_row, dtype=object).sum(axis=1)
            array_count_ls.append(object_array)

        # self.df1['result'] = self.df1.map(lambda x: my_function2(x, df2_array))