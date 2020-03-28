import csv
from csv import writer
from csv import reader
 
counter=0
list_username=[]
with open('DataSet_with_Usernames.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if row[5]=='0':
            list_username.append(row[12])


with open('openUsers.csv', 'w') as f:
		f.write("Username\n")
		for item in list_username:
			f.write("%s\n" % item)
