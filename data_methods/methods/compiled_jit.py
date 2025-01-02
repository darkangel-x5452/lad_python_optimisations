import numba
import pandas as pd
from numba import njit
from numba.typed import Dict, List

from utils.logger import log_execution_time
from utils.tools import create_dataset


@njit(nopython=True)
def count_past_matches(row: set, combinations: List[set]):
    # Initialize dictionary to store match counts by length
    count_dict = Dict.empty(key_type=numba.int64, value_type=numba.int64)

    # Pre-set count_dict with zero values for all possible match lengths (0 to 6)
    for i in range(7):  # Assuming match lengths are between 0 and 6
        count_dict[i] = 0

    # Iterate over the combinations
    for num in combinations:
        match_count = 0
        # Loop through elements in the combination and the row to count matches
        for elem in num:
            if elem in row:
                match_count += 1

        # Increment the match count for the corresponding length
        count_dict[match_count] += 1

    return count_dict


class JitCompile:
    def __init__(self, large_size: int =10000):
        data_size_large = large_size
        data_size_small = 1000
        self.df1 = create_dataset(col_id="A", size=data_size_large)
        self.df2 = create_dataset(col_id="B", size=data_size_small)

    @log_execution_time
    def run_transformation2(self):
        # df1_array = self.df1.to_numpy()
        # df2_array = self.df2.to_numpy()

        a_array = self.df1.to_numpy()
        b_array = self.df2.to_numpy()
        a_list = [set(a_row) for a_row in a_array]
        b_list = List(set(b_row) for b_row in b_array)

        a_match_count = pd.DataFrame({"normal_list": a_list}, index=self.df1.index)

        a_match_count["match_dict"] = a_match_count["normal_list"].map(lambda x: count_past_matches(x, b_list))
        return
