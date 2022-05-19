#!/dev/usr python

import pandas as pd
from operator import itemgetter

class Merge():

    def __init__(self):
        self.fld_left:dict = {}
        self.fld_right:dict = {}

    def join(self, left_data, right_data, join_condition, left_key, right_key):
        df_left = pd.DataFrame(left_data)
        df_right = pd.DataFrame(right_data)
        result = pd.merge(df_left, df_right, how =join_condition, left_on=left_key, right_on=right_key)
        result = result.fillna(' ')
        tmp = result.to_dict('index')
        data = []
        for _ in tmp.keys():
            data.append(tmp[_])
        return data
