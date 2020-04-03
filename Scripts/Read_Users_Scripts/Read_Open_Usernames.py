import csv
from csv import writer
from csv import reader
 
counter=0
list_username=[]
with open('/home/belericks7/Documenti/BigData/Project/SCRAPIAML/NewDataset.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        list_username.append(row[16])


with open('/home/belericks7/Documenti/BigData/Project/SCRAPIAML/251-500real.txt', 'w') as f:
		f.write("Username\n")
		for item in list_username:
			f.write("%s\n" % item)
