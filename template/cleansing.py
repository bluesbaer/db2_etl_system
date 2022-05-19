#!/dev/usr python

from tools import etl_cleansing as etl

def run(data):

    # RULEDEFINITION STRING
    # fieldname:rule:character:mappingtable

    # Example for mappingtable
    # map = [
    #        [['like1','like2','like...','likeN'],'text1'],
    #        [[ ... ], text...],
    #        [['likea','likeb','like...','likez'],'textN']
    #     ]
    
    id_map_data = [
        [[10,11,12,13,14,15,16,17,18,19],100],
        [[20,21,22,23,24,25,26,27,28,29],200],
        [[30,31,32,33,34,35,36,37,38,39],300],
        [[40,41,42,43,44,45,46,47,48,49],400],
        [[90,91,92,93,94,95,96,97,98,99],900],
    ] 

    rules = ["NACHNAME:UPPER::",
             "SEIT:DATE::",
             "ALTER:INTEGER::",
             "ID:MAP::id_map",
             "manager:SPLIT:' ':"]

    # --------------------------------------------------------------------------------------------------------------------------
    """ Executable - Please don't change """
    # --------------------------------------------------------------------------------------------------------------------------
    proc = etl.Cleansing()
    proc.load_map(id_map=id_map_data)
    data = proc.cleanup(data, rules)
    return data
