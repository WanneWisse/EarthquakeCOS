import pandas as pd
def load_data_exp_1(file_name):
    df = pd.read_csv(file_name,  low_memory=False)
    return df