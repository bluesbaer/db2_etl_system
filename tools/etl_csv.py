#!/dev/usr python3


import csv


class Csv():

    def read_data(self,file_name,seperator):
        data:list = []
        with open(file_name, 'r') as csv_file:
            file_reader = csv.DictReader(csv_file, delimiter=seperator)
            for row in file_reader:
                data.append(dict(row))
        return data


if __name__ == '__main__':
    reader = Csv()
    content = reader.read_data('F:\\PROJEKTE\\PYTHON\\vpython\\db2_etl_system\\tools\\TEST.csv',';')
    for _ in content:
        print(_)