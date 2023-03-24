import pandas as pd
import numpy as np
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .drop(columns=['Movie Info', 'Distributor', 'Release Date', 'Movie Runtime', 'License', 'Unnamed: 0'])
          .assign(**{'Genre': lambda x: x['Genre'].str.lower().str.replace('[^a-zA-Z0-9\s]', '').str.strip()})
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(**{'Release Year': lambda x: x['Title'].str[-5:-1]})
          .assign(**{'Title': lambda x: x['Title'].str[:-6]})
      )

    # Make sure to return the latest dataframe

    return df2 
