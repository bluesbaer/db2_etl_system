#!/dev/usr python

from tools import etl_preformat as etl

def run(data_in):

    """ Definition of the input-format """
    # --------------------------------------------------------------------------------------------------------------------------
    # SOURCE_FORMAT for DB
    # pre_format = ""
    # src_format = {'ID':'', 'NAME':'', 'SURENAME':'', 'AGE':'', 'DEPARTMENT_ID':'', 'SINCE':''}
    # 
    # SOURCE_FORMAT for CSV
    pre_format = ""
    src_format = {'ID':'', 'PRENAME':'', 'POSTNAME':'', 'AGE':'', 'DEPT_ID':'', 'SINCE':''}
    # 
    # SOURCE_FORMAT for JSON
    # pre_format = 'personal'
    # src_format = {'id':'', 'vorname':'', 'nachname':'', 'alter':'', 'abteilung':'', 'datum':''}
    # 
    # SOURCE_FORMAT for FIX
    # pre_format = ""
    # src_format = {'ID':'0:2', 'NAME':'2:12', 'SURENAME':'12:23', 'AGE':'23:25', 'DEPARTMENT_ID':'25:26', 'SINCE':'26:'}
    # --------------------------------------------------------------------------------------------------------------------------
    """ Datatype of the input-fields """
    # --------------------------------------------------------------------------------------------------------------------------
    # DATATYPE mapping for DB
    # src_type = {'ID':'int', 'NAME':'str', 'SURENAME':'str', 'AGE':'int', 'DEPARTMENT_ID':'int', 'SINCE':'date'}
    # 
    # DATATYPE mapping for CSV
    src_type = {'ID':'int', 'PRENAME':'str', 'POSTNAME':'str', 'AGE':'int', 'DEPT_ID':'int', 'SINCE':'date'}
    # 
    # DATATYPE mapping for JSON
    # src_type = {'id':'int', 'vorname':'str', 'nachname':'str', 'alter':'int', 'abteilung':'int', 'datum':'date'}
    # 
    # DATATYPE mapping for FIX
    # src_type = {'ID':'int', 'NAME':'str', 'SURENAME':'str', 'AGE':'int', 'DEPARTMENT_ID':'int', 'SINCE':'date'}
    # --------------------------------------------------------------------------------------------------------------------------
    """ Definition of the target-format (field-sequence) """
    # --------------------------------------------------------------------------------------------------------------------------
    # TARGET_FORMAT for DB
    # trg_format = ['ID','SURENAME','NAME','AGE','DEPARTMENT_ID','SINCE']
    # 
    # TARGET_FORMAT for CSV
    trg_format = ['ID','POSTNAME','PRENAME','AGE','DEPT_ID','SINCE']
    # 
    # TARGET_FORMAT for JSON
    # trg_format = ['id','nachname','vorname','alter','abteilung','datum']
    # 
    # TARGET_FORMAT for FIX
    # trg_format = ['ID','SURENAME','NAME','AGE','DEPARTMENT_ID','SINCE']
    # --------------------------------------------------------------------------------------------------------------------------
    """ Definition of the fieldname for the data-output """
    # --------------------------------------------------------------------------------------------------------------------------
    trg_name = ['ID','NACHNAME', 'VORNAME', 'ALTER', 'ABTEILUNG','SEIT']

    # --------------------------------------------------------------------------------------------------------------------------
    """ Executable - Please don't change """
    # --------------------------------------------------------------------------------------------------------------------------
    proc = etl.Preformat()
    data = proc.format(data_in,src_format,src_type,trg_format,trg_name,pre_format)
    return data


#src_format = {'l.ID':'', 'l.NACHNAME':'', 'l.VORNAME':'', 'l.ALTER':'', 'l.ABTEILUNG':'', 'l.SEIT':'', 'r.id':'', 'r.department-name':'', 'r.manager_0':'', 'r.manager_1':''}
#src_type = {'l.ID':'int', 'l.NACHNAME':'str', 'l.VORNAME':'str', 'l.ALTER':'int', 'l.ABTEILUNG':'int', 'l.SEIT':'date', 'r.id':'int', 'r.department-name':'str', 'r.manager_0':'str', 'r.manager_1':'str'}
#trg_format = ['l.ID', 'l.NACHNAME', 'l.VORNAME', 'l.ALTER', 'r.department-name', 'r.manager_0', 'r.manager_0']
#trg_name = ['ID', 'NACHNAME', 'VORNAME', 'ALTER', 'MGR_NACHNAME', 'MGR_VORNAME']