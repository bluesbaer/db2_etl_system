#!/dev/usr python

from tools import etl_cleansing as etl

def run(data):

    # Example for mappingtable (ID-Mapping)
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

    # Example for mappingtable (IF_THEN-Mapping)
    # map = [
    #        [[ "IF field, condition, value " ],[ "THEN field=value" ]],
    #        [[ "IF field, condition, value " ],[ "THEN field=value" ]],
    #        [[ "IF field, condition, value " ],[ "THEN field=value" ]]
    #    ]
    if_map_age = [
        [[ "row['ALTER'] < 30" ],[ "ALTER=JUNG" ]],
        [[ "row['ALTER'] > 40" ],[ "ALTER=ALT" ]],
        [[ "row['ALTER'] >= 30 and row['ALTER'] <= 40" ],[ "ALTER=MIDDLE" ]]
    ]

    # RULEDEFINITION STRING
    # rules = ["fieldname:rule:character:mappingtable",
    #          "fieldname:rule:character:mappingtable",
    #          "fieldname:rule:character:mappingtable"]
    rules = ["NACHNAME:UPPER::",
             "SEIT:DATE::",
             "ALTER:INTEGER::",
             "ID:MAP::id_map",
             "ALTER:IF_THEN::if_map",
             "manager:SPLIT:' ':"]

    # --------------------------------------------------------------------------------------------------------------------------
    """ Executable - Please don't change """
    # --------------------------------------------------------------------------------------------------------------------------
    proc = etl.Cleansing()
    proc.load_map(id_map=id_map_data, if_map = if_map_age)
    data = proc.cleanup(data, rules)
    return data
