from sklearn.model_selection import train_test_split
import pandas as pd

def read_data(file_name):
    try:
        return pd.read_csv(file_name)
    except IOError:
        return "Error: File does not appear to exist."

def split(name_dataset, prop_test):
    return train_test_split(name_dataset, test_size = prop_test)
