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

def xs2xs(iter_1 = None, iter_2 = None, name_1 = 'iter_1', name_2 = 'iter_2', values = None):
    '''
    This function is intended to check whether two iterables have the same values, i.e. whether a 1 to 1 mapping is possible.
    Provided iter_1 and iter_2, xs2xs checks whether there are values in one of them that are absent in the other.
    It returns a data frame where the first field lists all values in either iterable; the second field indicates how many occurrences
    of the element are present in iter_1; the third field ndicates how many occurrences of the element are present in iter_2. The
    data frame is ordered as to show first the elements present in only one of the two iterables.
    '''
    # By default the function will use all values present in at leas one of the two iterables
    if values == None:
        values = list(set(iter_1) | set(iter_2)

    # Defining the output dataframe:
    # The first column will contain a list of unique values
    r = pd.DataFrame()
    r['selected_values'] = pd.Series(values.unique())

    # Other fields will count the occurrences of the selected values in each iterable
    count_1 = f'occurrences in {name_1}'
    count_2 = f'occurrences in {name_2}'

    # Turning input iterables to Series for easier manipulation
    i1 = pd.Series(iter_1)
    i2 = pd.Series(iter_2)

    # Count occurrences of each unique value in the first iterator, managing NaN values
    r[count_1] = r[values].map(lambda x: i1.value_counts()[x] if x in i1.value_counts() else i1.isna().sum() if pd.isna(x) else 0)

    # Count occurrences of each unique value in the second iterator, managing NaN values
    r[count_2] = r[values].map(lambda x: i2.value_counts()[x] if x in i2.value_counts() else i2.isna().sum() if pd.isna(x) else 0)

    # Show absent values first
    r = r.sort_values(by=[count_1, count_2], ascending=[True, True])

    # Print stuff that is good to know:
    # 1. The number of NaNs in each iterator
    nans_1 = i1.isna().sum()
    nans_1_relative = nans_1 / len(i1) * 100
    nans_2 = i2.isna().sum()
    nans_2_relative = nans_2 / len(i2) * 100
    # 2. The percentage of 1 to 1 mapping
    unmatched = ((r[count_1] == 0) | (r[count_2] == 0)).sum()
    unmatched_relative = unmatched / len(r) * 100
    bijective_mapping_relative = 100 - unmatched_relative

    print(f'Number of NaNs in {name_1}: {nans_1} ({nans_1_relative:.2f}%)')
    print(f'Number of NaNs in {name_2}: {nans_2} ({nans_2_relative:.2f}%)')
    print(f'Percentage of unmatched values: {unmatched_relative:.2f}%')
    print(f'Percentage of bijective mapping: {bijective_mapping_relative:.2f}%')

    return r

def xs2ys(iter_1, iter_2):
    '''
    This function is intended to check whether two columns of a dataframe form couples that define 
    a 1 to 1 function, a many to 1 function, a 1 to many relation, or a many to many relation.
    It will work with any two same length iterables, but remember: it's very sensitive to sorting.
    '''
    i1 = pd.Series(iter_1)
    i2 = pd.Series(iter_2)
