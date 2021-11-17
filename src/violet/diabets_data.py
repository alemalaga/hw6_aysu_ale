# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:32:15 2021

@author: FDN-Aysu
"""

from sklearn.model_selection import train_test_split
import pandas as pd
import hw5
from hw5 import split

class SplitClass:
    def __init__(self,data_name):
        self.data_name =data_name
       
    def read_data(self, data_name):     
        return pd.read_csv(data_name)
    
    def train_test(self,data):
        return split(data,0.1)

name = "sample_diabetes_mellitus_data.csv"
df = SplitClass(name)
aysu=df.read_data(name)  
a,b=df.train_test(aysu)

class Preprocessor:
    def __init__(self,data_name):
        self.data_name=data_name
    def clean_nan(self,df):
        df.dropna(subset = ["age","gender","ethnicity"], inplace=True)
        return df
    def fill_nan(self,df):
        h_mean=df["height"].mean()
        w_mean=df["weight"].mean()
        df["height"].fillna(h_mean, inplace=True)
        df["weight"].fillna(w_mean, inplace=True)
        return df
ale = Preprocessor(aysu)
new_df=ale.clean_nan(aysu)
very_new=ale.fill_nan(aysu)

class Transfrom(Preprocessor):
    def __init__(self,):
        super().__init__(df):
            