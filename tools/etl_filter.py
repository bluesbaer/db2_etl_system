#!/dev/usr python

import datetime


class Filter():

    def __init__(self):
        pass

    def filter_engine(self, data_in, criteria):
        out_data:list = []
        # criteria = criteria.replace("§daten§","row")
        for row in data_in:
            if eval(criteria) == True:
                out_data.append(row)
        return out_data

    def deduplicate(self, data, key_list, key_match):
        tmp_key:list = []
        now_key:list = []
        data_out:list = []
        tmp_row:dict = {}
        if key_match == 'FIRST':
            for row in data:
                for key in key_list:
                    now_key.append(row[key])
                if now_key != tmp_key:
                    tmp_key = now_key
                    data_out.append(row)
                now_key:list = []
        elif key_match == 'LAST':
            for key in key_list:
                tmp_key.append(data[0][key])
            for row in data:
                for key in key_list:
                    now_key.append(row[key])
                if now_key != tmp_key:
                    tmp_key = now_key
                    data_out.append(tmp_row)
                    tmp_row = row
                else:
                    tmp_row = row
                now_key:list = []
            data_out.append(row)
        return data_out