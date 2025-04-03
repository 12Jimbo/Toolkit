import pandas as pd

def occurrences(seq, item):
    '''
    Auxiliary function returning the indexes of all occurrences of item in a sequence
    (it returns all positions at which an item can be found in a list)
    '''
    indexes = [index for (index, x) in enumerate(seq) if x == item]
    return indexes

def map_col2col(series_1, series_2):
    '''
    given 2 Series of the same length, an element x of series_1 is said to map to y in series_2
    if they happen have the same positional index at least once.
    The functions returns a DataFrame whether each element of series_1
    maps to each element of series_2.
    
    Build a table where indexes are unique elements from series1 and columns unique elements from
    series 2
    '''
    
    indexes = series_1.sort_values().unique()
    columns = series_2.sort_values().unique()
    matches = pd.DataFrame(index = indexes, columns = columns, data = False)
    
    for x in indexes:
        indexes_x_in_s1 = occurrences(series_1, x)   # positions of x in s1
        images_of_x_in_s2 = series_2[indexes_x_in_s1].unique()    # values y of s2 in the positions foud for x
        for y in columns:
            matches.loc[x, y] = y in images_of_x_in_s2
    return matches


def foreign_k2k(series_1, series_2, df1_name = 'table1', df2_name = 'table2', n_matches = -1, mode = '>'):
    '''
    Arguments: 
     1. two series passed as df1.series and df2.series.
     2. the name of df1 and the name of df2
     3. number of matches and a conditional selector
    
    Returns by Default: a data frame of 2 columns, where the first is series_1. 
    The second indicates for each element in series_1, the number of matches (same values)
    found in series_2. 
    If n_matches and mode are specified, only the values with the
    selected number of matches are returned.
    Example: n_matches = 0 and mode = '=' will return all values in series 1 that don't match
    any value in series 2.
    
    mode possible values: '=', '<', '>', '!='
    '''
    # Defining column names for the output dataframe:
    c_1 = df1_name + '.' + series_1.name + '_values' 
    c_2 = df2_name + '.' + series_2.name
    c_2 = 'matches_in_'+c_2+' '+mode+' '+str(n_matches)
    
    # Turning input series to lists:
    l_1 = list(series_1)
    l_2 = list(series_2)
    
    # Calculating mathces in series_2 for each element in series_1:
    matches = [l_2.count(i) for i in l_1]
    
    # Create DataFrame for series_1 vs matches in series_2
    df = pd.DataFrame({c_1: l_1, c_2: matches})
    
    df = df.drop_duplicates()

    if mode == '=':
        return df[df[c_2] == n_matches]
    if mode == '>':
        return df[df[c_2] > n_matches]
    if mode == '<':
        return df[df[c_2] < n_matches]
    if mode == '!=':
        return df[df[c_2] != n_matches]
