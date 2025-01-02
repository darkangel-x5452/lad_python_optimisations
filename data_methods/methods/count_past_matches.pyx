# count_past_matches.pyx

from libc.stdlib cimport malloc, free
from cython cimport boundscheck, wraparound
from typing import List, Set

@boundscheck(False)  # Disable bounds checking
@wraparound(False)  # Disable negative indexing
def count_past_matches(Set[int] row, List[Set[int]] combinations):
    # Initialize dictionary to store match counts by length
    count_dict = {i: 0 for i in range(7)}  # Pre-set count_dict with zero values for all possible match lengths

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