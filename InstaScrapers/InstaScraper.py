import csv
from io import StringIO
import os
import requests
import json
import time
import random
from datetime import datetime
import datetime
from datetime import timedelta
from igramscraper.instagram import Instagram


"""Scrape Instagram Profile"""

"""
Get the local time in day, day_number month year hour minute seconds format
"""
def get_time(epoch):
	a=time.strftime('%m/%d/%y %H:%M:%S', time.localtime(epoch))
	return a

"""
Delete 'OfficialDataSet.csv' file if exists
"""
def delete_data():
	if os.path.exists("OfficialDataSet.csv"):
		os.remove("OfficialDataSet.csv")

"""
Add the header at the "OfficialDataSet.csv" file
"""
def add_header():
	with open('OfficialDataSet.csv', mode='w') as csv_file:
		fieldNames = ['Profile Pic','Nums/Length Username','Full Name Words','Nums/Length Fullname','Bio Length','External Url','Private','Verified','Business','#Posts','#Followers','#Following','Last Post Recent']
		writer = csv.DictWriter(csv_file, fieldnames = fieldNames, lineterminator='\n')
		writer.writeheader()

"""
Create the "'OfficialDataSet.csv' file if not exists and add a row to the dataset, containing the informations about an account.
	x is the name of the file, data is the data to add to the file
"""
def add(x, data):
	# Open the file in append-mode
	with open(x, mode = 'a', encoding="utf-8") as csv_file:
		# Define the columns name
		fieldNames = ['Profile Pic','Nums/Length Username','Full Name Words','Nums/Length Fullname','Bio Length','External Url','Private','Verified','Business','#Posts','#Followers','#Following','Last Post Recent']
		# assign every data properties to the right fieldname
		writer = csv.DictWriter(csv_file, fieldnames = fieldNames, lineterminator='\n')
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
			list.append(f'{row["Username"]}')
			line_count += 1
		print(f'Processed {line_count} lines.')

"""
Define a new empty list which will contains the accounts username
"""
usernameList = []

delete_data()
addUsername(usernameList)
add_header()

print(usernameList)

"""
For every account in the usernameList takes his informations and add it
	to the OfficialDataSet.csv file
"""

instagram = Instagram()

for account in usernameList:
	details={}
	u=account.strip()
	url='https://www.instagram.com/'+u+'/'
	account = instagram.get_account(account)

	print('\nAccount info:')

	picUrl=account.get_profile_picture_url()
	if "44884218_345707102882519_2446069589734326272_n.jpg" in picUrl:
		details['Profile Pic']='0'
	else:
		details['Profile Pic']='1'
	print('Has Profile Pic:-\t',details['Profile Pic'])

	count=0
	for char in str(account.username):
		if char.isnumeric()==True:
			count=count+1
	if len(account.username)==0 or count==0:
		result=0
	else:
		result=count/len(account.username)
	details['Nums/Length Username']=str(round(result,3))
	print('Nums/Length Username:-\t',details['Nums/Length Username'])

	# using split() to count words in string
	result = len(account.full_name.split())
	details['Full Name Words']=str(result)
	print('Full Name Words:-\t',details['Full Name Words'])

	count=0
	for char in str(account.full_name):
		if char.isnumeric()==True:
			count=count+1
	if len(account.full_name)==0 or count==0:
		result=0
	else:
		result=count/len(account.full_name)
	details['Nums/Length Fullname']=str(round(result,3))
	print('Nums/Length Fullname:-\t',details['Nums/Length Fullname'])

	details['Bio Length']=str(len(account.biography))
	print('Bio lenght:-\t\t',details['Bio Length'])

	if account.external_url=='':
		details['External Url']='0'
	else:
		details['External Url']='1'
	print('External Url:-\t\t',details['External Url'])

	if account.is_private==False:
		details['Private']='0'
	else:
		details['Private']='1'
	print('Is private:-\t\t',details['Private'])

	if account.is_verified==False:
		details['Verified']='0'
	else:
		details['Verified']='1'
	print('Is verified:-\t\t',details['Verified'])

	details['#Posts']=str(account.media_count)
	print('Number of posts:-\t',details['#Posts'])

	details['#Followers']=str(account.followed_by_count)
	print('Number of followers:-\t',details['#Followers'])

	details['#Following']=str(account.follows_count)
	print('Number of follows:-\t',details['#Following'])

	time.sleep(random.randrange(25,35))

	r=requests.get(url)
	body=r.text.split('window._sharedData = ')[1].split(';</script>')[0]
	data=json.loads(body)
	user=data['entry_data']['ProfilePage'][0]['graphql']['user']

	if user['is_business_account']==False:
		details['Business']='0'
	else:
		details['Business']='1'
	print('Is Business:-\t\t',details['Business'])

	if details['Private']=='0':
		if details['#Posts'] == '0':
			details['Last Post Recent']='Null'
			print('Is Last Post Recent:-\t',details['Last Post Recent'])
		else :
			timestamp = int(user['edge_owner_to_timeline_media']['edges'][0]['node']['taken_at_timestamp'])
			if datetime.datetime.today() - datetime.datetime.strptime(get_time(timestamp), '%m/%d/%y %H:%M:%S') < timedelta(days=180):
				details['Last Post Recent']='1'
			else:
				details['Last Post Recent']='0'
			print('Is Last Post Recent:-\t',details['Last Post Recent'])
	else:
		details['Last Post Recent']='Null'
		print('Is Last Post Recent:-\t',details['Last Post Recent'])
	add('OfficialDataSet.csv',details)
	time.sleep(random.randrange(25,35))
print('Result saved as OfficialDataSet.csv')
