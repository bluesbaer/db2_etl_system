
import pandas as pd

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


df_left = pd.DataFrame(left_data)
df_right = pd.DataFrame(right_data)

result = pd.merge(df_left, df_right, how ='inner', left_on='f1', right_on='id')
tmp = result.to_dict('index')
data = []
for _ in tmp.keys():
    data.append(tmp[_])

