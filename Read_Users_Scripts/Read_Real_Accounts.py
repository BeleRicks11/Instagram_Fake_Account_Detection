import csv
import os

"""
Delete "reals_users.txt" file if exists
"""
def delete_data():
	if os.path.exists("reals_users.txt"):
		os.remove("reals_users.txt")

"""
Read the "dataset.txt" file and write the username of the real accounts in a .txt file
"""
def readReals():
	# Take the fake users from "dataset.csv" and insert them in a list
	with open('dataset.csv', mode='r', encoding="utf-8") as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		users = []
		for row in csv_reader:
			if(row["fake"] == '0'):
				users.append(row["username"].strip())
				line_count += 1
		print(f'Found {line_count} real accounts and added to the reals_users.txt.')
	# Insert the item of the users list in a .txt file
	with open('reals_users.txt', 'w') as f:
		f.write("Username\n")
		for item in users:
			f.write("%s\n" % item)

readReals()