#!/dev/usr python3


class Fix():

    def __init__(self):
        pass

    def read_data(self,filename):
        data:list = []
        with open(filename, 'r') as fixfile:
            row = fixfile.readline()
            while row:
                row = row.replace('\n','')
                data.append(row)
                row = fixfile.readline()
        return data

# -- TESTROUTINE -------------------------------------------------
if __name__ == '__main__':
    content = Fix()
    data = content.read_data('F:\\PROJEKTE\\PYTHON\\vpython\\db2_etl_system\\tools\\TEST.fix')
    print(data)
