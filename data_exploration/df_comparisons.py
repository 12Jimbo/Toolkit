import pandas as pd

# Here's an auxiliary function returning the list of indexes of an item in an iterable:
# (the funxtion says all positions at which an item can be found in a list)
def occurrences(seq, item):
    indexes = [index for (index, x) in enumerate(seq) if x == item]
    return indexes

def map_col2col(series_1, series_2):
    # given 2 Series of the same length, an element x of series_1 is said to map to y in series_2
    # if they happen have the same positional index at least once.
    # The functions returns a DataFrame whether each element of series_1
    # maps to each element of series_2.
    
    # Build a table where indexes are unique elements from series1 and columns unique elements from
    # series 2
    indexes = series_1.sort_values().unique()
    columns = series_2.sort_values().unique()
    matches = pd.DataFrame(index = indexes, columns = columns, data = False)
    
    for x in indexes:
        indexes_x_in_s1 = occurrences(series_1, x)   # positions of x in s1
        images_of_x_in_s2 = series_2[indexes_x_in_s1].unique()    # values y of s2 in the positions foud for x
        for y in columns:
            matches.loc[x, y] = y in images_of_x_in_s2
    return matches
