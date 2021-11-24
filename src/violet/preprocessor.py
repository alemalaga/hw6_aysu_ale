# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:22:38 2021

@author: Aysu
"""

import pandas as pd

class Preprocessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def clean_nan(self, clean_columns):
        self.df.dropna(subset = clean_columns, inplace=True)
        # return self.df

    def fill_nan(self, fill_columns):
        for x in fill_columns:
            xmean=self.df[x].mean()
            self.df[x].fillna(xmean, inplace=True)