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
            
# data_prep = Preprocessor(train_data)
# data_prep.clean_nan(['age', 'gender', 'ethnicity'])
# data_prep.fill_nan(['height', 'weight'])
