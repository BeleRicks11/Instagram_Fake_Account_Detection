import csv
from csv import writer
from csv import reader
 
counter=0
list_username=[]
with open('/home/belericks7/Documenti/BigData/Project/Datasets/Copia.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if int(row[9])<10000 and row[11]=='0':
            counter+=1

print(counter)