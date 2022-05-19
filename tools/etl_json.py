#!/dev/usr python3

import json

class Json():

    def __init__(self):
        pass

    def read_data(self,filename):
        with open(filename) as json_file:
            data = json.load(json_file)
        return data

if __name__ == '__main__':
    driver = Json()
    data = driver.read_data('F:\\PROJEKTE\\PYTHON\\vpython\\db2_etl_system\\tools\\TEST.json')
    print(data)