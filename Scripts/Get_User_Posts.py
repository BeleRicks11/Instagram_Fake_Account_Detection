from igramscraper.instagram import Instagram
import time
from datetime import timedelta
import datetime
import random

# If account is public you can query Instagram without auth

instagram = Instagram()

number_of_posts = 100

medias = instagram.get_medias("riya_12335", number_of_posts)
#Percentuale di post effettuati in un giorno sul totale dei post effettuati
max=0
post=1
i=0
while i<len(medias):
    for x in range(i+1,len(medias)):
        if time.strftime('%m/%d/%y', time.localtime(medias[i].created_time)) == time.strftime('%m/%d/%y', time.localtime(medias[x].created_time)):
            post+=1
    if post>max:
        max=post
    i+=post
    post=1
percent=(max*100)/len(medias)
print("Percentuale:",percent)


#indice di attività mensile tra i post dell'ultimo anno
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
print("Post nei vari mesi:",month)
print("Indice di attività:",average)

#media mippi 
total_mippi=0
for media in medias:
    total_mippi+=media.likes_count
average_mippi=total_mippi/len(medias)
print("Media mippi:",average_mippi)


#media mippi 
total_comments=0
for media in medias:
    comments = instagram.get_media_comments_by_id(media.identifier, 10000)
    total_comments+=len(comments['comments'])
    time.sleep(random.randrange(5,10))
average_comments=total_comments/len(medias)
print("Media commenti:",average_comments)  

