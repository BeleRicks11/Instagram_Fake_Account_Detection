import os

"""
Define a list containing the really existing users, with no duplicates
"""
realUsers = []

"""
This go through the list of the existing users and adds it to the list.
 If any duplicate is found, it is not considered twice and does't save it a second time.
"""
if os.path.exists("reals copy.txt"):
	lines_seen = set() # holds lines already seen
	for line in open("reals copy.txt", "r"):
		if line not in lines_seen: # not a duplicate
			lines_seen.add(line)
			realUsers.append(line)
		else: 
			print(line)
	os.remove("reals copy.txt") # delete the "real_users.txt" file
	# Create a new "reals copy.txt" containing the real users with no duplicates
	outfile = open("reals copy.txt", "w")
	for user in realUsers:    	# add the user firstly appended 
		outfile.write(user)		# in the list	
	outfile.close()


