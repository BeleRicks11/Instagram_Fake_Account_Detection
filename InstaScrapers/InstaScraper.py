import csv
from io import StringIO
import os
import requests
import json
import time

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

"""
Create the "data.csv" file if not exists and add a row to the dataset, containing the informations about an account.
    x is the name of the file, data is the data to add to the file
"""
def add(x, data):
    # Open the file in append-mode
	with open(x, mode = 'a', encoding="utf-8") as csv_file:
		# Define the columns name
		fieldNames = ['Username','UserID','Full Name','Is Private','Followers','Following','Total Medias','Is Business','last time','Bio']
		# assign every data properties to the right fieldname
		writer = csv.DictWriter(csv_file, fieldnames = fieldNames)
        # add a row with the new data to the file
		writer.writerow(data)

"""
Read the "users.txt" file and append every username (in a row) to a list
"""
def addUsername(list):
    with open('users.txt', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            list.append(f'{row["username"]}')
            line_count += 1
        print(f'Processed {line_count} lines.')

"""
Define a new empty list which will contains the accounts username
"""
usernameList = []

delete_data()
addUsername(usernameList)

print(usernameList)

"""
For every account in the usernameList takes his informations and add it 
    to the data.csv file
"""
for account in usernameList:
	details={}
	u=account.strip()
	url='https://www.instagram.com/'+u+'/'

	r=requests.get(url)
	body=r.text.split('window._sharedData = ')[1].split(';</script>')[0]
	data=json.loads(body)
	user=data['entry_data']['ProfilePage'][0]['graphql']['user']
	print('\t\t===BIO===\n'+user['biography']+'\n\t\t=========')
	details['Bio']=user['biography']
	print('Username :-\t\t'+user['username'])
	details['Username']=user['username']
	print('User Id :-\t\t'+user['id'])
	details['UserID']=user['id']
	print('Full Name:-\t\t'+user['full_name'])
	details['Full Name']=user['full_name']
	print('Is Private:-\t\t'+str(user['is_private']))
	details['Is Private']=user['is_private']
	print('Follower Count :-\t'+str(user['edge_followed_by']['count']))
	details['Followers']=str(user['edge_followed_by']['count'])
	print('Following Count:-\t'+str(user['edge_follow']['count']))
	details['Following']=str(user['edge_follow']['count'])
	print('Media Count:-\t\t'+str(user['edge_owner_to_timeline_media']['count']))
	details['Total Medias']=str(user['edge_owner_to_timeline_media']['count'])
	print('is Business Account:-\t'+str(user['is_business_account']))
	details['Is Business']=str(user['is_business_account'])
	if not details['Is Private']:
		timestamp = int(user['edge_owner_to_timeline_media']['edges'][0]['node']['taken_at_timestamp'])
		details['last time']=get_time(timestamp)
		print('Last Post Time:-\t'+details['last time'])
	add('data.csv',details)
	time.sleep(5)
print('Result saved as data.csv')