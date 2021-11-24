from sklearn.model_selection import train_test_split
import pandas as pd

def read_data(file_name):
    try:
        return pd.read_csv(file_name)
    except IOError:
        return "Error: File does not appear to exist."

def split(name_dataset, prop_test):
    return train_test_split(name_dataset, test_size = prop_test)


class SplitClass:
    def __init__(self, data_name):
        self.data_name = data_name
    
    def train_test(self, prop_test):
        all_data = read_data(self.data_name)
        return split(all_data, prop_test)
    


# name = "../../diabetes/sample_diabetes_mellitus_data.csv"
# example = SplitClass(name)
# train_data,test_data=example.train_test(0.1)
