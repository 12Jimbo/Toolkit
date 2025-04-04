# A few dataframes, series and lists for testing functions
import pandas as pd
import numpy as np

data_multitype = {
    'Column1': [1, 2.5, 3, 4.8, 5],     # Mixed integers and floats
    'Column2': ['A', 'B', 'C', 'D', 5], # Strings and an integer
    'Column3': [True, False, np.nan, 1, 'Mixed']  # Booleans, NaN, integer, and string
}

df_multitype = pd.DataFrame(data_multitype)

data_nans = {
    'Column1': [1, np.nan, np.nan, 4, 5],       # Contains NaN values
    'Column2': ['A', 'B', np.nan, np.nan, 'E'], # Contains NaN values
    'Column3': [True, np.nan, np.nan, True, False]  # Contains NaN values
}

df_nans = pd.DataFrame(data_nans)

df_maps1 = pd.DataFrame(
    {
        'a': [1, 2, 3, 4, 3],
        'b': [1, 3, 1, 3, 1],
        'c': ['lollo', 'gigio', 'lollo', 'gigio', 'lollo']
    })

df_maps2 = pd.DataFrame(
    {
        'a': [1, 2, 3, 4],
        'b': [1, 1, 3, 5]
    }
)

data_text = {
    'Column1': ['##apple##', 'banana!!', '%%cherry%%', 'date@@', '@@elderberry@@'],  # Repeated special characters
    'Column2': [' A1 ', ' B2 ', ' C3 ', ' D4 ', ' E5 '],                             # Leading/trailing spaces
    'Column3': ['@hello@', '!!world!!', ' python ', 'rocks@@', None]                # Mixed issues
}

df_text = pd.DataFrame(data_text)