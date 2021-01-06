import pandas as pd
import os
import glob

# Removing non-digit characters from `production_budget`, `domestic_gross` and `worldwide_gross` 
def remove_non_digit_chars(string):
    return float(''.join(c for c in string if c.isdigit()))

# Splitting 'genres' column's comma separated values into separated lines 
def split_column(df, col):
    s = df[col].str.split(',').apply(pd.Series, 1).stack()
    s.index = s.index.droplevel(-1)
    s.name = col
    df2 = df.drop(col, axis=1).join(s)
    df2[col] = df2[col].apply(lambda x: x.strip())
    return df2

# Check to see whether a movie is made by 1 of 6 major studios:
major_studios = ['Warner Bros', 'Walt Disney', '20th Century Fox', 'Paramount', 'Sony', 'Universal']
def if_major_studio(string):
    return any(studio in string for studio in major_studios)

# Get .csv.gz files and files' names from 'data/zippedData' directory
def import_files():
    # Accessing the files stored in 'data/zippedData'
    based_path = os.sep.join(['data', 'zippedData'])
    files = glob.glob(based_path + "/*.csv.gz")
    filenames = ["_".join(file.split('/')[-1].split('.')[:-2]) for file in files]
    return files, filenames
