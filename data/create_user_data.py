import os

userfile = os.getcwd() + '\\raw-files\\raw_user_data.txt'
targetfile = os.getcwd() + '\\raw-files\\user_v1.csv'
namefile = os.getcwd() + '\\raw-files\\name_list.txt'

# Note that this only works for 2500 users or less. Both name_list.txt
# and raw_user_data.txt were created with exactly 2500 unique entries.

userct = 0
user_ary = []
delim = b','

# Get list of names
namef = open(namefile, 'r')
names = [line.rstrip('\n') for line in namef]
namef.close()

userf = open(userfile, 'r')
wrtf = open(targetfile, 'wb')
for line in userf:	
	user_id, song_id, play_count = line.strip().split('\t')
	
	if user_id not in user_ary:
		user_ary.append(user_id)
		userct += 1 # Only works if lines with same user_id are grouped together
		
		name_from_ary = names[userct - 1]
		
		user_id = bytes(user_id, 'utf-8') # Username is primary key
		# Using user_id only to match raw_user_data with appropriate song_id
		fname = name_from_ary.split(' ')[0]
		lname = name_from_ary.split(' ')[1]
		username = bytes(fname + lname[:3], 'utf-8')
		email = bytes(fname[:2] + lname + '@wisc.edu', 'utf-8')
		fname = bytes(fname, 'utf-8')
		lname = bytes(lname, 'utf-8')
		
		password_hash = bytes("sha1$23424$asdlf34535435", 'utf-8')
		create_date = bytes('1999-12-07 06:45:35', 'utf-8') 
			
		# Hash doesn't actually work--think about creating a real hash
		# Create_dt in format 'YYYY-MM-DD HH:MM:SS'
		
		wrtf.write(username + delim + email + delim + fname + delim +
				lname + delim + password_hash + delim + create_date + b'\r\n') 
				
userf.close()
wrtf.close()
        
