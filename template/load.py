#!/dev/usr python

from tools import etl_db as etl


def run(data):

    trg_server ="db2amdmt"
    trg_port = "60220"
    trg_database = "AMDMT"
    trg_user = "db2amdmt"
    trg_pwd = "ibm#db2"
    trg_schema = "STRG"
    trg_table = "T_TARGET"
    trg_key:list = ['ID']
    trg_data:list = ['NACHNAME','VORNAME','ALTER','SEIT','ABTEILUNG','MGR_NACHNAME','MGR_VORNAME']


    # --------------------------------------------------------------------------------------------------------------------------
    """ Executable - Please don't change """
    # --------------------------------------------------------------------------------------------------------------------------
    trg_record = trg_key + trg_data

    target = etl.Db2()
    target.connect(trg_server, trg_port, trg_database, trg_user, trg_pwd)
    target.write_data(data, trg_schema, trg_table, trg_key, trg_data, trg_record)
    
    return data