import csv
from io import StringIO
import os
import requests
import json
import time
import random
from igramscraper.instagram import Instagram 


"""Scrape Instagram Profile"""

"""
Get the local time in day, day_number month year hour minute seconds format
"""
def get_time(epoch):
	a=time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
	return a

"""
Delete "data.csv" file if exists
"""
def delete_data():
	if os.path.exists("data.csv"):
		os.remove("data.csv")
	if os.path.exists("fake_users.txt"):
		os.remove("fake_users.txt")

"""
Add the header at the "data.csv" file
"""
def add_header():
	with open('data.csv', mode='w') as csv_file:
		fieldNames = ['Username','UserID','Full Name','Is Private','Followers','Following','Total Medias','Is Business','last time','Bio','Profile Pic Url', 'External Url','Is Verified']
		writer = csv.DictWriter(csv_file, fieldnames = fieldNames)
		writer.writeheader()

"""
Create the "data.csv" file if not exists and add a row to the dataset, containing the informations about an account.
	x is the name of the file, data is the data to add to the file
"""
def add(x, data):
	# Open the file in append-mode
	with open(x, mode = 'a', encoding="utf-8") as csv_file:
		# Define the columns name
		fieldNames = ['Username','UserID','Full Name','Is Private','Followers','Following','Total Medias','Is Business','last time','Bio','Profile Pic Url', 'External Url','Is Verified']
		# assign every data properties to the right fieldname
		writer = csv.DictWriter(csv_file, fieldnames = fieldNames)
		# add a row with the new data to the file
		writer.writerow(data)

"""
Read the "users.txt" file and append every username (in a row) to a list
"""
def addUsername(list):
	with open('dataset.csv', mode='r', encoding="utf-8") as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		for row in csv_reader:
			list.append(f'{row["username"]}')
			line_count += 1

		print(f'Processed {line_count} lines.')

"""
Add the header at the "fake_users.txt" file
"""
def add_headerFake():
	with open('fake_users.txt', mode='w') as csv_file:
		fieldNames = ['Username']
		writer = csv.DictWriter(csv_file, fieldnames = fieldNames)
		writer.writeheader()

"""
Create the "fake_users.txt" file if not exists and add a row to the dataset, containing the informations about an account.
	x is the name of the file, data is the data to add to the file
"""
def addFake(x, data):
	# Open the file in append-mode
	with open(x, mode = 'a', encoding="utf-8") as csv_file:
		# Define the columns name
		fieldNames = ['Username']
		# assign every data properties to the right fieldname
		writer = csv.DictWriter(csv_file, fieldnames = fieldNames)
		# add a row with the new data to the file
		writer.writerow(data)

"""
Read the "dataset.txt" file and write the username of the fake accounts in a .txt file
"""
def readFakes():	
	with open('dataset.csv', mode='r', encoding="utf-8") as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		for row in csv_reader:
			if(row["fake"] == '1'):
				users = {}
				users['Username'] = row["username"].strip()
				addFake('fake_users.txt', users)
				line_count += 1
		print(f'Found {line_count} fake accounts and added to the fakes.txt.')

"""
Define a new empty list which will contains the accounts username
"""
usernameList = []

delete_data()
addUsername(usernameList)
add_header()

add_headerFake()
readFakes()

print(usernameList)

"""
For every account in the usernameList takes his informations and add it 
	to the data.csv file
"""

instagram = Instagram()

for account in usernameList:
	details={}
	u=account.strip()
	url='https://www.instagram.com/'+u+'/'

	account = instagram.get_account(account)
	print('\nAccount info:')
	details['UserID']=account.identifier
	print('User Id:-\t\t'+details['UserID'])

	details['Username']=account.username
	print('Username:-\t\t'+details['Username'])

	details['Full Name']=account.full_name
	print('Full name:-\t\t'+details['Full Name'])

	details['Bio']=account.biography
	print('Biography:-\t\t'+details['Bio'])

	details['Profile Pic Url']=account.get_profile_picture_url()
	print('Profile Pic Url:-\t'+details['Profile Pic Url'])

	details['External Url']=account.external_url
	print('External Url:-\t\t',details['External Url'])

	details['Total Medias']=account.media_count
	print('Number of posts:-\t',details['Total Medias'])

	details['Followers']=account.followed_by_count
	print('Number of followers:-\t',details['Followers'])

	details['Following']=account.follows_count
	print('Number of follows:-\t',details['Following'])

	details['Is Private']=account.is_private
	print('Is private:-\t\t',details['Is Private'])

	details['Is Verified']=account.is_verified
	print('Is verified:-\t\t',details['Is Verified'])

	time.sleep(10)

	r=requests.get(url)
	body=r.text.split('window._sharedData = ')[1].split(';</script>')[0]
	data=json.loads(body)
	user=data['entry_data']['ProfilePage'][0]['graphql']['user']
	print('Is Business Account:-\t'+str(user['is_business_account']))
	details['Is Business']=str(user['is_business_account'])
	if not details['Is Private']:
		if details['Total Medias'] == '0':
			details['last time']="Null"
			print('Last Post Time:-\t',details['last time'])
		else :
			timestamp = int(user['edge_owner_to_timeline_media']['edges'][0]['node']['taken_at_timestamp'])
			details['last time']=get_time(timestamp)
			print('Last Post Time:-\t',details['last time'])
	else:
		details['last time']="Null"
		print('Last Post Time:-\t',details['last time'])

	add('data.csv',details)
	time.sleep(random.randrange(25,35))
print('Result saved as data.csv')