# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:33:47 2021

@author: Aysu
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self, col_features, col_target, niter = 500):
        self._col_features = col_features
        self._col_target = col_target
        self._niter = niter
        self.model = LogisticRegression(penalty='l2', C=100.0, 
                           fit_intercept=True, 
                           intercept_scaling=1, 
                           solver='liblinear', max_iter=niter)
            
    def train(self, df: pd.DataFrame):
        X = df[self._col_features]
        y = df[self._col_target].values.ravel()
        self.model.fit(X, y)
        
    def predict(self,  df: pd.DataFrame):
        Xtest = df[self._col_features]
        return self.model.predict_proba(Xtest)[:,1]