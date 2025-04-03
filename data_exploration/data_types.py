import pandas as pd
  
def col_types(df):
  '''
  In: a data frame df
  Out: prints the number of element types found in each column of a given df
  '''
  for i in df.columns:
        print(
            df[i].map(type).value_counts(),
            '\n NaN values: ',
            df[i].isna().sum(),
            '\n'
    )


def nan2nan(df, col_1_name, col_2_name):
    '''
    Given 2 columns in a data frame df, this function
    prints the number of NaNs in the first,
    The number of NaNs in the second,
    And the number fo rows where both cols have NaN value
    '''

    col_1 = col_1_name 
    col_2 = col_2_name
    
    # Number of NaN rows in col_1:    
    nans_1 = pd.isna(df[col_1]).sum()
    # Number of NaN rows in col_2:
    nans_2 = pd.isna(df[col_2]).sum()
    # Number of rows where both col_1 and col_2 are NaN:
    nans_1and2 = (pd.isna(df[col_1]) * pd.isna(df[col_2])).sum()
    
    print(
    'NaN values in {}: '.format(col_1),
    nans_1,
    '\n\nNaN values in {}: '.format(col_2),
    nans_2,
    '\n\nNaN values in the same row for both {} and {}: '.format(col_1, col_2),
    nans_1and2
)
