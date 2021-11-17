from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def split(name_dataset, prop_test):
    return train_test_split(name_dataset, test_size = prop_test)
