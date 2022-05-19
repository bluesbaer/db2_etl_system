#!/dev/usr python

from db2_etl_system.tools import etl_db, etl_csv, etl_json, etl_xml, etl_fix
# import tools
def run():
    """ Define source for extract """
    # IF SOURCE IS DB2-DATABASE
    # source = etl_db.Db2()
    
    # IF SOURCE IS CSV-FILE
    # source = etl_csv.Csv()

    # IF SOURCE IS JSON-FILE
    # source = etl_json.Json()

    # IF SOURCE IS FIXLENGTH
    source = etl_fix.Fix()
    
    """ Extract Data from the source """
    # EXTRACT FROM DB2-DATABASE
    # source.connect('db2amdmt',60220,'AMDMT','db2amdmt','ibm#db2')
    # data = source.read_data('''SELECT * FROM SSRC.T_SOURCE''')
    
    # EXTRACT FROM CSV-FILE
    # data = source.read_data('F:\\PROJEKTE\\PYTHON\\vpython\\db2_etl_system\\tools\\TEST.csv',';')
    
    # EXTRACT FROM JSON-FILE
    # data = source.read_data('F:\\PROJEKTE\\PYTHON\\vpython\\db2_etl_system\\tools\\TEST.json')
    
    # EXTRACT FROM FIXLENGTH
    data = source.read_data('F:\\PROJEKTE\\PYTHON\\vpython\\db2_etl_system\\tools\\TEST.fix')
    
    """ Return the Data """
    return data