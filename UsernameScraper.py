from igramscraper.instagram import Instagram # pylint: disable=no-name-in-module
from time import sleep

instagram = Instagram()
instagram.with_credentials('pietro.sonnini00', 'F&#yig4x0j5D')
instagram.login(force=False,two_step_verificator=True)

sleep(20) # Delay to mimic user

username = 'am.e.lie'
followings = []
account = instagram.get_account(username)
sleep(1)
followings = instagram.get_following(account.identifier, 150, 50, delayed=True) # Get 150 followers of 'username', 100 a time with random delay between requests

for following in followings['accounts']:
    if following.is_private==False:
        print(following.username)