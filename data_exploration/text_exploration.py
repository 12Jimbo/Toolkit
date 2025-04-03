import pandas as pd

def initials(s):
    '''
    Given a Series of strings, it retruns all unique first characters
    '''
    s = s.map(lambda x: x[0] if isinstance(x, str) else x)
    return s.value_counts(dropna = False)

def finals(s):
    '''
    Given a Series of strings, it retruns all unique first characters
    '''
    s = s.map(lambda x: x[-1] if isinstance(x, str) else x)
    return s.value_counts(dropna = False)
