import cython
import pandas as pd
from data_methods.methods.count_past_matches import count_past_matches

from utils.logger import log_execution_time
from utils.tools import create_dataset

class CythonMethod:
    def __init__(self, large_size: int = 10000):
        data_size_large = large_size
        data_size_small = 1000
        self.df1 = create_dataset(col_id="A", size=data_size_large)
        self.df2 = create_dataset(col_id="B", size=data_size_small)

    @log_execution_time
    def run_transformation1(self):
        if cython.compiled:
            print("Running as cython")
        else:
            print("Running as python")

        a_array = self.df1.to_numpy()
        b_array = self.df2.to_numpy()
        a_list = [set(a_row) for a_row in a_array]
        b_list = [set(b_row) for b_row in b_array]

        a_match_count = pd.DataFrame({"normal_list": a_list}, index=self.df1.index)

        a_match_count["match_dict"] = a_match_count["normal_list"].map(lambda x: count_past_matches(x, b_list))
        return
