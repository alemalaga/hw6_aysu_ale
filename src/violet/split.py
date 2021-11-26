import hw5
from hw5 import read_data, split


class SplitClass:
    def __init__(self, data_name):
        self.data_name = data_name
    
    def train_test(self, prop_test):
        all_data = read_data(self.data_name)
        return split(all_data, prop_test)

# name = "../../diabetes/sample_diabetes_mellitus_data.csv"
# example = SplitClass(name)
# train_data,test_data=example.train_test(0.1)
