#!/dev/usr python

import re

class Cleansing():

    def __init__(self):
        pass

    def load_map(self, **kwargs):
        self.map_intern = kwargs

    def cleanup(self, data, rules):
        out_data:list = []
        for row in data:
            for tmp_rule in rules:
                fld, rule, character, map = tmp_rule.split(':')
                if rule in ['UPPER', 'LOWER', 'STRIP']:
                    row = self.clear_simple_text(row, fld, rule)
                elif rule in ['SPLIT']:
                    row = self.split_text(row, fld, character)
                elif rule in ['MAP']:
                    row = self.map_data(row, fld, map)
                elif rule in ['DATE']:
                    row = self.clear_date(row,fld)
                elif rule in ['IF_THEN']:
                    row = self.if_then(row, fld, map)
            out_data.append(row)
        return out_data

    def clear_simple_text(self, row, fld, rule):
        if rule == 'UPPER':
            row[fld] = row[fld].upper()
        elif rule == 'LOWER':
            row[fld] = row[fld].lower()
        elif rule == 'STRIP':
            row[fld] = row[fld].strip()
        return row

    def split_text(self, row, fld, character):
        tmp:list = []
        if row != None:
            if character in [',',';','|',':','!']:
                cont = str(row[fld])
                tmp = cont.split(character)
            else:
                cont = str(row[fld])
                tmp = cont.split(' ')
            del row[fld]
            for nr, _ in enumerate(tmp):
                row[f"{fld}_{nr}"] = _
            return row

    def map_data(self, row, fld, map):
        for number in range(len(self.map_intern[map])):
            search = self.map_intern[map][number][0]
            target = self.map_intern[map][number][1]
            if row[fld] in search:
                row[fld] = target
                return row

    def clear_date(self, row, fld):
        data:str = ""
        status = re.search("\d{4}-\d{2}-\d{2}",str(row[fld]))
        if status == None:
            if self.check_year(row, fld) == True:
                if self.check_month(row, fld) == True:
                    if self.check_day(row, fld) == True:
                        data = f'{row[fld][:4]}-{row[fld][4:6]}-{row[fld][6:]}'
                    else:
                        data = f'{row[fld][:4]}-{row[fld][4:6]}-01'
                else:
                    data = f'{row[fld][:4]}-01-01'
            else:
                data = f'1900-01-01'
        else:
            data = status.group()
        row[fld] = data
        return row

    def check_year(self, row, fld):
        flag = False
        if int(row[fld][:4]) >= 1900 and int(row[fld][:4]) <= 2999:
            flag = True
        return flag

    def check_month(self, row, fld):
        flag = False
        if int(row[fld][4:6]) >= 1 and int(row[fld][4:6]) <= 12:
            flag = True
        return flag

    def check_day(self, row, fld):
        flag = False
        if int(row[fld][4:6]) in [1,3,5,7,8,10,12] and int(row[fld][6:]) >= 1 and int(row[fld][6:]) <=31:
            flag = True
        elif int(row[fld][4:6]) in [4,6,9,11] and int(row[fld][6:]) >= 1 and int(row[fld][6:]) <=30:
            flag = True
        elif int(row[fld][:4]) %4 == 0 and int(row[fld][4:6]) in [2] and int(row[fld][6:]) >= 1 and int(row[fld][6:]) <=29:
            flag = True
        elif int(row[fld][:4]) %4 != 0 and int(row[fld][4:6]) in [2] and int(row[fld][6:]) >= 1 and int(row[fld][6:]) <=28:
            flag = True
        return flag
    
    def if_then(self, row, fld, map):
        for line in self.map_intern[map]:
            chk = line[0]
            #string = line[1][0]
            target, result = str(line[1][0]).split('=')
            try:
                if eval(chk[0]) == True:
                    row[target] = result
            except:
                pass
        return row
