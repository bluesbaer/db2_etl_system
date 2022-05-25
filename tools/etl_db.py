#!/dev/usr python3

import ibm_db

class Db2():

    def __init__(self):
        pass
        
    def connect(self,server,port,database,user,pwd):
        conn_str:str = ""
        conn_str = f"DATABASE={database}; HOSTNAME={server}; PORT={port}; "
        conn_str += f"PROTOCOL=TCPIP; UID={user}; PWD={pwd}"
        try:
            self.connection = ibm_db.connect(conn_str,"","")
        except Exception as e:
            print(f"Unable for user '{user}' to connect to database '{database}'")
            print(f"ERROR:{e}")
        
    def read_data(self,sql):
        row:dict = {}
        data:list = []
        try:
            cursor = ibm_db.exec_immediate(self.connection,sql)
            row = ibm_db.fetch_assoc(cursor)
            while row != False:
                data.append(row)
                row = ibm_db.fetch_assoc(cursor)
        except Exception as e:
            print("Der Datenzugriff hat nicht funktioniert")
            print(f"ERROR:{e}")
        return data
        
    def write_data(self, data, trg_schema, trg_table, trg_key, trg_data, trg_record):
        act_trg_key:str = ""
        act_src_key:str = ""
        act_src_dat:str = ""
        act_key_str:str = ""
        act_dat_str:str = ""
        for _ in trg_key:
            act_trg_key += "TRG."+_+","
        act_trg_key = act_trg_key[:-1]
        for row in data:
            for _ in row.keys():
                if _ in trg_key:
                    act_src_key += "'"+str(row[_])+"',"
                    act_key_str += str(_)+","
                elif _ in trg_data:
                    act_src_dat += "'"+str(row[_])+"',"
                    act_dat_str += str(_)+","
            
            # MERGE INTO strg.t_target TRG
            #     USING (SELECT 'RECORD' FROM sysibm.sysdummy1) SRC
            #     ON (('10') = (TRG.ID))
            #     WHEN MATCHED THEN
            #         UPDATE SET
            #         (NACHNAME,VORNAME,ALTER,SEIT,ABTEILUNG,MGR_NACHNAME,MGR_VORNAME) = ('GRÜN','FRANZ','ALT','1900-01-01','DEMOLITION','GRUNZ','FLUNZ')
            #     WHEN NOT MATCHED THEN
            #     INSERT
            #         (ID,NACHNAME,VORNAME,ALTER,SEIT,ABTEILUNG,MGR_NACHNAME,MGR_VORNAME) VALUES ('10','GRÜN','FRANZ','ALT','1900-01-01','DEMOLITION','GRUNZ','FLUNZ')

            sql = f"MERGE INTO {trg_schema}.{trg_table} AS TRG "
            sql += f"USING (SELECT 'RECORD' FROM SYSIBM.SYSDUMMY1) SRC "
            sql += f"ON (({act_src_key[:-1]}) = ({act_trg_key})) "
            sql += f"WHEN MATCHED THEN "
            sql += f"UPDATE SET "
            sql += f"({act_dat_str[:-1]}) = ({act_src_dat[:-1]}) "
            sql += f"WHEN NOT MATCHED THEN "
            sql += f"INSERT "
            sql += f"({act_key_str[:-1]},{act_dat_str[:-1]}) "
            sql += f"VALUES ({act_src_key[:-1]},{act_src_dat[:-1]})"
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ibm_db.exec_immediate(self.connection,sql)            
            sql = ""
            act_src_key = ""
            act_src_dat = ""
            act_key_str = ""
            act_dat_str = ""
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    def db_import(self,data,table,mapping):
        pass
        
# -- TESTROUTINE -------------------------------------------------
if __name__ == '__main__':
    driver = Db2()
    driver.connect('db2amdmt',60220,'AMDMT','db2amdmt','ibm#db2')
    db_data = driver.read_data('SELECT * FROM SSRC.T_SOURCE')
    print(db_data)
