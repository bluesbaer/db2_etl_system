#!/dev/usr python

# system

# etl
from template import extract, preformat, filter, merge, cleansing, transform, delta, build, load

print("-- START WORKFLOW --------------------------------------------------------------")
print("-- START EXTRACT ---------------------------------------------------------------")
data = extract.run()
print(data)
print("-- START PREFORMAT -------------------------------------------------------------")
data = preformat.run(data)
print(data)
print("-- START FILTER ----------------------------------------------------------------")
data = filter.run(data)
print(data)
print("-- START MERGE -----------------------------------------------------------------")
data = merge.run(data)
print(data)
print("-- START CLEANSING -------------------------------------------------------------")
data = cleansing.run(data)
print(data)
#print("-- START TRANSFORM -------------------------------------------------------------")
#data = transform.run(data)
#print(data)
#print("-- START DELTA -----------------------------------------------------------------")
#data = delta.run(data)
#print(data)
#print("-- START BUILD -----------------------------------------------------------------")
#data = build.run(data)
#print(data)
#print("-- START LOAD ------------------------------------------------------------------")
#data = load.run(data)
#print(data)
print("-- END WORKFLOW ----------------------------------------------------------------")
