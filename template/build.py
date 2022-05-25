#!/dev/usr python

from datetime import datetime
from tools import etl_csv as etl
from tools import etl_build

def run(data):

    # Filename and seperator are optional
    filename:str = ""
    seperator:str = ""

    # As a result there are two possible options
    # 1. Output as CSV (for external usage)
    # 2. Output as STREAM (for ETL-LOAD)
    result:str = ""
    # result = "CSV"
    # --------------------------------------------------------------------------------------------------------------------------
    """ Executable - Please don't change """
    # --------------------------------------------------------------------------------------------------------------------------
    if filename == "":
        filename:str = f"{datetime.now().strftime('build.%Y%m%d%H%M%S%f')}"
    if seperator == "":
        seperator = ","
    if result == 'CSV':
        proc = etl.Csv()
        proc.write_data(data, filename, seperator)
        return filename
    else:
        # proc = etl_build.Build()
        # output = proc.build_data(data)
        # return output
        return data
    
