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
        
    def write(self,sql):
        pass
        
    def db_import(self,data,table,mapping):
        pass
        

if __name__ == '__main__':
    driver = Db2()
    driver.connect('db2amdmt',60220,'AMDMT','db2amdmt','ibm#db2')
    db_data = driver.read_data('SELECT * FROM SSRC.T_SOURCE')
    print(db_data)
