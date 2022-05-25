#!/dev/usr python

from datetime import datetime
import re

class Preformat():

    def __init__(self):
        pass

    def format(self,data_in,src_format,src_type,trg_format,trg_name=[],preformat=""):
        self.preformat = preformat
        self.src_format = src_format
        self.src_type = src_type
        self.trg_format = trg_format
        self.trg_name = trg_name if len(trg_name) > 0 else trg_format
        data_out:list = []
        if len(data_in) > 0:
            if preformat != "":
                data_in = data_in[preformat]
            data_out = self.iterate_row(data_in)
        return data_out

    def iterate_row(self,data_in):
        data:list = []
        for row in data_in:
            data.append(self.iterate_field(row))
        return data

    def iterate_field(self,row_in):
        row:dict = {}
        for fld,name in zip(self.trg_format, self.trg_name):
            length = self.src_format[fld]
            row[name] =self.map_data(row_in,fld,length)
        return row

    def map_data(self,row_in,fld,length):
        if length == '':
            temp = row_in[fld]
            temp = self.map_type(temp,fld)
        else:
            from_pos, to_pos = length.split(':')
            if to_pos != '':
                temp = row_in[int(from_pos):int(to_pos)]
                temp = self.map_type(temp,fld)
            else:
                temp = row_in[int(from_pos):]
                temp = self.map_type(temp,fld)
        return temp

    def map_type(self,data,fld):
        if self.src_type[fld] == 'int':
            try:
                data = int(data)
            except:
                pass
        if self.src_type[fld] == 'float':
            try:
                data = float(data)
            except:
                pass
        elif self.src_type[fld] == 'str':
            data = str(data).strip()
        elif self.src_type[fld] == 'date':
            try:
                data = self.format_date(data)
            except:
                pass
        elif self.src_type[fld] == 'datetime':
            try:
                data = self.format_timestamp(data)
            except:
                pass
        return data

    def format_date(self,data):
        data = str(data)
        status = re.search("\d{4}-\d{2}-\d{2}",data)
        if status == None:
            data = f'{data[:4]}-{data[4:6]}-{data[6:]}'
        else:
            data = status.group()
        data = datetime.strptime(data,'%Y-%m-%d').date()
        return data

    def format_timestamp(self,data):
        data = str(data)
        status = re.search("\d{4}-\d{2}-\d{2}-\d{2}.\d{2}",data)
        if status == None:
            data = f'{data[:4]}-{data[4:6]}-{data[6:8]}-{data[8:10]}.{data[10:12]}.{data[12:]}'
        else:
            data = status.group()
        data = datetime.strptime(data, '%Y-%m-%d-%H.%M.%S')
        return data

