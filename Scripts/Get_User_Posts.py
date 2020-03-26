from igramscraper.instagram import Instagram
import time
from datetime import timedelta
import datetime

# If account is public you can query Instagram without auth

instagram = Instagram()

medias = instagram.get_medias("_riccardo.fava_", 100)
days=0
post=0
i=0
while i<len(medias):
    for x in range(i+1,len(medias)):
        if time.strftime('%m/%d/%y', time.localtime(medias[i].created_time)) == time.strftime('%m/%d/%y', time.localtime(medias[x].created_time)):
            post+=1
    if post!=0:
        i+=post
        days+=1
    i+=1
    post=0
print(days)

def get_time(epoch):
    a=time.strftime('%m/%d/%y', time.localtime(epoch))
    return a


month=[0,0,0,0,0,0,0,0,0,0,0,0]

def check_date(media):
    date_to_check = datetime.datetime.strptime(get_time(media.created_time), '%m/%d/%y')
    if datetime.datetime.today() - date_to_check < timedelta(days=30):
        month[0]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=60):
        month[1]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=90):
        month[2]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=120):
        month[3]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=150):
        month[4]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=180):
        month[5]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=210):
        month[6]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=240):
        month[7]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=270):
        month[8]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=300):
        month[9]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=330):
        month[10]+= 1
    elif datetime.datetime.today() - date_to_check < timedelta(days=360):
        month[11]+= 1

for media in medias:
    check_date(media)

total=0
for i in month:
    total+=i
average=total/12
print(month)
print(average)