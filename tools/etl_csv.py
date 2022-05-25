#!/dev/usr python3


import csv


class Csv():

    def read_data(self,file_name,seperator=","):
        data:list = []
        with open(file_name, 'r') as csv_file:
            file_reader = csv.DictReader(csv_file, delimiter=seperator)
            for row in file_reader:
                data.append(dict(row))
        return data

    def write_data(self, data, filename, seperator=","):
        csv_columns:list = []
        for key in data[0].keys():
            csv_columns.append(key)

        try:
            with open(filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=seperator)
                writer.writeheader()
                for line in data:
                    writer.writerow(line)
        except IOError:
            print("I/O error")


# -- TESTROUTINE -------------------------------------------------
if __name__ == '__main__':
    reader = Csv()
    content = reader.read_data('F:\\PROJEKTE\\PYTHON\\vpython\\db2_etl_system\\tools\\TEST.csv',';')
    for _ in content:
        print(_)