import random
from igramscraper.instagram import Instagram 


"""proxies = {
    'http': 'http://80.211.37.70',
    'https': 'http://80.211.37.70',
}"""

instagram = Instagram()
#instagram.set_proxies(proxies)

account_name_list=["neymarjr"]

account = instagram.get_account('hjejendbdnsnshsb')
print('Account info:')
print('Id', account.identifier)
print('Username', account.username)
print('Full name', account.full_name)
print('Biography', account.biography)
print('Profile pic url', account.get_profile_picture_url())
print('External Url', account.external_url)
print('Number of published posts', account.media_count)
print('Number of followers', account.followed_by_count)
print('Number of follows', account.follows_count)
print('Is private', account.is_private)
print('Is verified', account.is_verified)

#print(random.randrange(25,35))
