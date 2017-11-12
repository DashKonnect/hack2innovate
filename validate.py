import csv
import pandas as pd

file1 = pd.read_csv("result.csv");
file1 = file1.sort_values(by=["FileName"]);
file1.to_csv('result_sorted.csv', index=False)

file2 = pd.read_csv("cross.csv");
file2 = file2.sort_values(by=["FileName"]);
file2.to_csv('cross_sorted.csv', index=False)

merged = file1.merge(file2, indicator=True, how='inner')
print(len(merged.values)/170)

# result_reader={}
# filename = "results3.csv"
# csvfile = open(filename)
# result_reader = csv.DictReader(csvfile)

# filename = "cross.csv"
# file = open(filename)
# reader = csv.DictReader(file)
# count = 0

# for key in reader.keys():
# 	if key in result_reader.keys():
# 		print(result_reader[key])


#or i in reader:
#for j in result_reader:
#	print("{},{}".format(i['FileName'],j['FileName']))
		#print(j['FileName'])
		#if i['FileName'] == j['FileName']:
		#	print("{} correct:{},prediction:{}".format(i['FileName'],i['Label'],j['Label']))
		#if i['FileName'] == j['FileName'] and i['Label'] == j['Label']:
		#	count +=1


