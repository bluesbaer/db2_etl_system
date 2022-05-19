#!/dev/usr python

from tools import etl_merge as etl

def run(data, data_1=[]):

    proc = etl.Merge()

    """ STATIC DATA """
    data_1 = [
        {'id':1, 'department-name':'Human Resource', 'manager':'Turner Doris'},
        {'id':2, 'department-name':'IT', 'manager':'Gans Gustav'},
        {'id':3, 'department-name':'Sales', 'manager':'Gross Friedrich'},
    ]

    """ List keyfields for data """
    left_key = ['ABTEILUNG']

    """ List keyfields for data_1 """
    right_key = ['id']

    """ SELECT JOIN CONDITION """
    join_condition = 'inner'
    # join_condition = 'left'
    # join_condition = 'right'
    # join_condition = 'full'

    # --------------------------------------------------------------------------------------------------------------------------
    """ Executable - Please don't change """
    # --------------------------------------------------------------------------------------------------------------------------
    data = proc.join(data, data_1, join_condition, left_key, right_key)
    return data