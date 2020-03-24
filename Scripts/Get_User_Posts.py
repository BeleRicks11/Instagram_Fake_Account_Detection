from igramscraper.instagram import Instagram

# If account is public you can query Instagram without auth

instagram = Instagram()

medias = instagram.get_medias("neymarjr", 10)
media = medias[1]

print(media)
account = media.owner
print(account)