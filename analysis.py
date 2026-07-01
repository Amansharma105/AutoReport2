import pandas as pd

def mean(df, column):
    return df[column].mean()

def median(df, column):
    return df[column].median()

def mode(df, column):
    return df[column].mode()[0]

def standard_deviation(df, column):
    return df[column].std()
