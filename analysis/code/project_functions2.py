def load_and_process(csv1,csv2):
    import pandas as pd
    import numpy as np
    import matplotlib.pylab as plt
    import seaborn as sns
    import re
    
    df1 = (pd.read_csv("../data/raw/Highest Holywood Grossing Movies.csv")
           .drop(columns=['Unnamed: 0', 'Movie Info', 'Release Date','License']))
    df1 = (
        df1
        .assign(**{'Hours': lambda x: x['Movie Runtime'].str.extract('(\d+)\shr\s*\d*\s*m*i*n*', expand=True)})
        .assign(**{'Minutes': lambda x: x['Movie Runtime'].str.extract('\d+\shr\s*(\d*)\s*m*i*n*', expand=True)})
        .apply(pd.to_numeric, errors = 'ignore')
        .assign(**{'Minutes': lambda x: x['Minutes'].fillna(0)})
        .assign(**{'Runtime (Min)': lambda x: round(((60 * x['Hours']) + x['Minutes']),0)})
        .drop(columns= ['Hours','Minutes','Movie Runtime'])
    )
    df2 = (pd.read_csv("../data/processed/Movie Aggregate Rating Data Final.csv")
           .drop(columns=['Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10'])
    )
    df2 = (
        df2
        .assign(**{'Imdb': lambda x: x['Imdb'].str.extract('(\d+\.*\d*)\s*\(*\d*\+*\)*', expand=True)})
        .assign(**{'Letterboxd': lambda x: x['Letterboxd'].str.extract('(\d+\.*\d*)\s*\(*\d*\+*\)*', expand=True)})
        .assign(**{'Rateyourmusic': lambda x: df2['Rateyourmusic'].str.extract('(\d+\.*\d*)\s*\(*\d*\+*\)*', expand=True)})
        .apply(pd.to_numeric, errors = 'ignore')
    )
    df2 = (
        df2
        .assign(**{'Imdb Standardized': lambda x: (x['Imdb']/10)*100})
        .assign(**{'Letterboxd Standardized': lambda x: (x['Letterboxd']/5)*100})
        .assign(**{'Rateyourmusic Standardized': lambda x: (x['Rateyourmusic']/5)*100})
        .drop(columns=['Imdb', 'Letterboxd','Rateyourmusic'])
        .assign(**{'Average Rating': lambda x: round(((x['Imdb Standardized'] + x['Letterboxd Standardized'] + x['Rateyourmusic Standardized'])/3),1)})
    )
    df3 = (
        pd.merge(
            df1,
            df2,
            how="outer",
            on='Title')
        .assign(**{'Worldwide Popularity': lambda x: round(((((x['World Sales (in $)']/x['World Sales (in $)'].max())*100)/2) + (x['Average Rating']/2)),1)})
        .dropna()
    )
    return df3