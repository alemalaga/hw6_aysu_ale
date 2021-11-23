import pandas as pd
import numpy as np
import hw5
from hw5 import read_data, split
from abc import ABCMeta, abstractmethod
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures


class SplitClass:
    def __init__(self, data_name):
        self.data_name = data_name
    
    def train_test(self, prop_test):
        all_data = read_data(self.data_name)
        return split(all_data, prop_test)

# name = "../../diabetes/sample_diabetes_mellitus_data.csv"
# example = SplitClass(name)
# train_data,test_data=example.train_test(0.1)

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
        # return self.df

# data_prep = Preprocessor(train_data)
# data_prep.clean_nan(['age', 'gender', 'ethnicity'])
# data_prep.fill_nan(['height', 'weight'])

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
    
# numeric_data = test_data.select_dtypes(include = ['float', 'int']).dropna()
# test_standardize = Standardize(numeric_data)
# answ_standardize = test_standardize.change()
# test_polynomial = Polynomial(numeric_data)
# answ_polynomial = test_polynomial.change(2)   

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

# features = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
#             'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
# target = ['diabetes_mellitus']
# test_model = Model(features, target, 500)
# test_model.train(train_data)
# test_model.predict(test_data.dropna())
