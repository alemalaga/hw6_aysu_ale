# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:32:15 2021

@author: FDN-Aysu
"""

from sklearn.model_selection import train_test_split
import pandas as pd
import hw5
from hw5 import split
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures


class SplitClass:
    def __init__(self,data_name):
        self.data_name =data_name
       
    def read_data(self, data_name):     
        return pd.read_csv(data_name)
    
    def train_test(self,data):
        return split(data,0.1)

name = "sample_diabetes_mellitus_data.csv"
df = SplitClass(name)
all_data=df.read_data(name)  
train_data,test_data=df.train_test(all_data)

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
data_prep = Preprocessor(all_data)
new_df=data_prep.clean_nan(all_data)
very_new=data_prep.fill_nan(all_data)


class Transform(ABC):
    @abstractmethod
    def standardize_feaures(self):
        pass
    
    @abstractmethod
    def polynomial_features(self):
        pass
    
    
class Standardize(Transform):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def standardize_feaures(self):
        scl = StandardScaler()
        self.scaled = scl.fit_transform(self.df)
        self.scaled = pd.DataFrame(self.scaled, columns = self.df.columns, index = self.df.index)
    
    def polynomial_features(self):
        pol = PolynomialFeatures(2)
        self.polynized = pol.fit_transform(self.df)
        pol_cols = pol.get_feature_names_out(self.df.columns)
        self.polynized = pd.DataFrame(self.polynized, columns = pol_cols, index = self.df.index)
    

class Model:
    def __init__(self, col_features: pd.DataFrame, col_target: pd.Series):
        self.col_features = col_features
        self.col_target = col_target
    
    def train(self):
        reg = LinearRegression()
        self.fitted = reg.fit(self.col_features, self.col_target)
        
    def predict(self):
        self.predict = self.fitted.predict(self.col_target)
        print(self.predict)


numeric_data = very_new.select_dtypes(include = ['float', 'int'])
   
numeric_data = numeric_data.dropna()
test_scaled = Standardize(numeric_data)
test_scaled.standardize_feaures()
test_scaled.polynomial_features()   
         
our_model = Model(test_scaled.polynized.drop('weight', axis = 1), test_scaled.polynized['weight'])
our_model.train()
our_model.predict()