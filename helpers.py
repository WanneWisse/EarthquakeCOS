import pandas as pd
def load_data_exp_1(file_name):
    df = pd.read_csv('tweets.csv',  low_memory=False)
    df = df[["content","language"]]
    return df