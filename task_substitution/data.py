# AUTOGENERATED! DO NOT EDIT! File to edit: 01_data.ipynb (unless otherwise specified).

__all__ = ['Dataset']

# Cell
import pandas as pd
import numpy as np

from .core import *

# Cell
class Dataset:
    def __init__(self, df, **kwargs):
        self.df = df
        self.missing_fld = kwargs['missing_fld']
        self.ignore_flds = kwargs['ignore_flds']
        self.cat_flds = kwargs['cat_flds']

    @property
    def target(self):
        return self.data[self.missing_fld]

    def remove_ignore_flds(self)->pd.DataFrame:
        if self.ignore_flds is not None:
            self.df = _ignore_flds(self.df, self.ignore_flds)
        return self.df

    def preprocess_categorical(self)->pd.DataFrame:
        cats = self.cat_flds if self.cat_flds else self.df.select_dtypes(include=['object']).columns
        for c, v in self.df.loc[:, cats].items():
            self.df.loc[:, c] = _preprocess_categorical(v)
        return self.df

    def preprocess(self):
        self.df = self.remove_ignore_flds()
        self.df = self.preprocess_categorical()

        return self.df

    @classmethod
    def split_train_test(cls, df, missing_fld):
        """
        Splits the dataframe into train and test dataset based on the rows having values
        for missing feature or not.
        """
        train, test = _split_train_test(df, missing_fld)
        return train, test