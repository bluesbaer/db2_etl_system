
import re
import datetime
from typing import ChainMap

txt = '1980-10-10'
x = re.search("\d\d\d\d-\d\d-\d\d", txt)
print(x)

txt = '19801010'
x = re.search("\d\d\d\d-\d\d-\d\d", txt)
print(x)

txt = '1980-10-10-12.15.30.000000'
x = re.search("\d{4}-\d{2}-\d{2}-\d{2}.\d{2}", txt)
print(x.span(), x.string, x.group())
pos_von = x.span()[0]
pos_bis = x.span()[1]
print(pos_von,pos_bis)

print("***********")

data:list = [
    {'F1':10, 'F2':'text', 'F3':datetime.date(1980, 10, 10)},
    {'F1':20, 'F2':'oh', 'F3':datetime.date(1970, 10, 10)},
    {'F1':30, 'F2':'ah', 'F3':datetime.date(1975, 10, 10)}
]

criteria = "row['F1'] > 10 and row['F2'] in ['text', 'ah']"

for row in data:
    if eval(criteria) == True:
        print(row)
    else:
        print('????')

print("***********")

d1 = {'F1':1, 'F2':'A'}
d2 = {'FA':1, 'FB':'X'}
for _ in d2.keys():
    d1[f"r.{_}"] = d2[_]

print(d1)

print("SPLIT with BLANK")

x = "Adam Bernd Christine Doris Egon Franz Georg"
print(x)
tmp = x.split(' ')
print(tmp)

print("####################################################")

id_map = [
    [[10,11,12,13,14,15,16,17,18,19],100],
    [[20,21,22,23,24,25,26,27,28,29],200],
    [[30,31,32,33,34,35,36,37,38,39],300],
    [[40,41,42,43,44,45,46,47,48,49],400]
] 

for row in id_map:
    print(row[0],row[1])

jdata = {"personal":[
    {"id":10, "name":"fritz"},
    {"id":20, "name":"franz"},
    {"id":30, "name":"hugo"},
]}   

jout = jdata['personal']
print(jout)

print("--- DE-Duplicate ---")

data = [
    {'id':10, 'part1':100, 'part2':'A'},
    {'id':20, 'part1':100, 'part2':'A'},
    {'id':30, 'part1':100, 'part2':'B'},
    {'id':40, 'part1':200, 'part2':'A'},
    {'id':50, 'part1':200, 'part2':'A'},
    {'id':60, 'part1':200, 'part2':'B'},
    {'id':70, 'part1':200, 'part2':'B'}
]

# RESULTAT: 10, 30, 40, 60 : FIRST
# RESULTAT: 20, 30, 50, 70 : LAST

key_list = ['part1','part2']
key_match = 'LAST'

def deduplicate(data,key_list,key_match):
    tmp_key:list = []
    now_key:list = []
    data_out:list = []
    tmp_row:dict = {}
    if key_match == 'FIRST':
        for row in data:
            for key in key_list:
                now_key.append(row[key])
            if now_key != tmp_key:
                tmp_key = now_key
                data_out.append(row)
            now_key:list = []
    elif key_match == 'LAST':
        for key in key_list:
            tmp_key.append(data[0][key])
        for row in data:
            for key in key_list:
                now_key.append(row[key])
            if now_key != tmp_key:
                tmp_key = now_key
                data_out.append(tmp_row)
                tmp_row = row
            else:
                tmp_row = row
            now_key:list = []
        data_out.append(row)
    return data_out

print(deduplicate(data,key_list,key_match))

print("--- MERGE ----------")

left_data = [
    {'id':10, 'f1':'A'},
    {'id':20, 'f1':'B'},
    {'id':30, 'f1':'B'},
    {'id':40, 'f1':'A'},
    {'id':50, 'f1':'B'},
    {'id':60, 'f1':'A'},
    {'id':70, 'f1':'A'},
    {'id':80, 'f1':'B'},
]

right_data = [
    {'id':'A', 'TEXT':'NEU'},
    {'id':'B', 'TEXT':'ALT'},
]

for left in left_data:
    for right in right_data:
        z = ChainMap(left, right)
        print(f"z:{z}")