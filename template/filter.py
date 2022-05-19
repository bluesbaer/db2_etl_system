#!/dev/usr python

import datetime
from tools import etl_filter as etl

def run(data):
    proc = etl.Filter()

    # Remove Duplicates
    # key_list : A list of fields in the record which identify if this is a duplicate or not
    # key_match: FIRST give back the first record with this key
    #            LAST give back the last record with this key
    # ---------------------------------------------------------------------------------------
    # key_list = ['key1', 'key2', ..., 'keyN']
    # key_match = 'FIRST' 
    # data = proc.deduplicate(data, key_list, key_match)
    
    # criteria = "row['ALTER'] >= 30 and row['ABTEILUNG'] in [1, 2, 3]"
    criteria = "row['ALTER'] >= 30"

    # --------------------------------------------------------------------------------------------------------------------------
    """ Executable - Please don't change """
    # --------------------------------------------------------------------------------------------------------------------------
    data = proc.filter_engine(data,criteria)
    return data