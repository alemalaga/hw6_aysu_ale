from sklearn.model_selection import train_test_split
import pandas as pd

class SplitClass:
    def __init__(self, data_name):
        self.data_name = data_name
    
    def train_test(self, prop_test):
        all_data = pd.read_csv(self.data_name)
        return train_test_split(all_data, test_size = prop_test)
    


# name = "../../diabetes/sample_diabetes_mellitus_data.csv"
# example = SplitClass(name)
# train_data,test_data=example.train_test(0.1)