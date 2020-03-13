import os

"""
Define a list containing the really existing users, with no duplicates
"""
realUsers = []

"""
This go through the list of the existing users and adds it to the list.
 If any duplicate is found, it is not considered twice and does't save it a second time.
"""
if os.path.exists("real_users2.txt"):
	lines_seen = set() # holds lines already seen
	for line in open("real_users2.txt", "r"):
		if line not in lines_seen: # not a duplicate
			lines_seen.add(line)
			realUsers.append(line)
		else: 
			print(line)
	os.remove("real_users2.txt") # delete the "real_users.txt" file
	# Create a new "real_users.txt" containing the real users with no duplicates
	outfile = open("real_users2.txt", "w")
	for user in realUsers:    	# add the user firstly appended 
		outfile.write(user)		# in the list	
	outfile.close()


