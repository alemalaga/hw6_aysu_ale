# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:26:36 2021

@author: Aysu
"""
import pandas as pd
from abc import ABCMeta, abstractmethod
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

class Transform(metaclass = ABCMeta):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @abstractmethod
    def change(self):
        return NotImplementedError    
    
class Standardize(Transform):

    def change(self):
        scl = StandardScaler()
        scl_df = scl.fit_transform(self.df)
        self.scaled = pd.DataFrame(scl_df, 
                                   columns = self.df.columns, 
                                   index = self.df.index)

class Polynomial(Transform):
    
    def change(self, npoly):
        pol = PolynomialFeatures(npoly)
        pol_df = pol.fit_transform(self.df)
        pol_cols = pol.get_feature_names_out(self.df.columns)
        self.polynized = pd.DataFrame(pol_df, 
                                      columns = pol_cols, 
                                      index = self.df.index)
    