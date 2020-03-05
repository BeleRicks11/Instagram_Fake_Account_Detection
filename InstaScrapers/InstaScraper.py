import requests
import json
import time
import csv

"""Scrape Instagram Profile"""
           
def get_time(epoch):
	a=time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
	return a

def add(x,data):
	with open(x, mode='a') as csv_file:
		fieldnames = ['Username','UserID','Full Name','Is Private','Followers','Following','Total Medias','Is Business','last time','Bio']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writerow(data)

account_name_list=["neymarjr", "_riccardo.fava_"]


for account in account_name_list:
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
		timestamp=int(user['edge_owner_to_timeline_media']['edges'][0]['node']['taken_at_timestamp'])
		details['last time']=get_time(timestamp)
		print('Last Post Time:-\t'+details['last time'])
	add('data.csv',details)
	time.sleep(10)

print('Result saved as data.csv')
