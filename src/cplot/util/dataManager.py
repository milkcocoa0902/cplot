import pandas as pd

class DataManager():
    def __init__(self, _src = None):
        if _src is not None:
            self.df_ = pd.read_csv(_src)
    
    def Read(self, _src = None, _delimiter = ',', _header = 0):
        if _src is None:
            return 
        self.df_ = pd.read_csv(_src, delimiter = _delimiter, header = _header, index_col = 0)

    def Write(self, _dst = None):
        if _dst is None:
            return
        self.df_.to_csv(_dst)

    def df(self):
        return self.df_
