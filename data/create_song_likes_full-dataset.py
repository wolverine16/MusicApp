import os
import random

user_file = os.getcwd() + '\\raw-files\\raw_user_data.txt'
song_file = os.getcwd() + '\\raw-files\\song_v1.csv'
target_file = os.getcwd() + '\\raw-files\\song_likes_v1.csv'
raw_namefile = os.getcwd() + '\\raw-files\\name_list.txt'


def get_line(file, position):
    start_position = position
    while True:
        file.seek(position)
        symbol = file.read(1)
        if symbol == '\n' and file.tell() != start_position + 1:  
        # Get line when we reach \n and \n was not the first match
            return file.readline().rstrip()

        elif position == 0:                                       
        # Get symbol plus the rest of the line when we reach start of file
            return symbol + file.readline().rstrip()

        else:
            position -= 1


def get_random_lines(file, num_of_lines):
    file.seek(0, 2) # Seek through end of file
    last_char = file.tell() - 1  # Avoid EOF

    lines = []
    for _ in range(num_of_lines):
        try:
            position = random.randint(0, last_char)
            lines.append(get_line(file, position))
        
        except UnicodeDecodeError:
            return " "
            
        except UnicodeEncodeError:
            return " "

    return lines


def main(userfile, songfile, targetfile):
    userf = open(userfile, 'r')
    songf = open(songfile, 'r')
    slf = open(targetfile, 'wb')
    
    delim = ','
    user_ary = []
    userct = 0
    
    # Get list of names
    raw_namef = open(raw_namefile, 'r')
    names = [line.rstrip('\n') for line in raw_namef]
    raw_namef.close()

    for line in userf:
        user_id, song_id, play_count = line.strip().split('\t')
        
        if user_id not in user_ary:
            user_ary.append(user_id)
            userct += 1 # Only works if lines with same user_id are grouped together
            
        name_from_ary = names[userct - 1]
            
        fname = name_from_ary.split(' ')[0]
        lname = name_from_ary.split(' ')[1]
        username = fname + lname[:3]

        
        
        #song_lines = " "
        #while song_lines == " ":
            #song_lines = get_random_lines(songf, 1)
        #song_id = song_lines[0].split(',')[0]
        
        slf.write(bytes(song_id + delim + username + delim + play_count +
            delim + str(random.uniform(3, 5)) + '\r\n', 'utf-8'))
        # For the rating, we pick random float b/w 3 and 5


    userf.close()
    songf.close()
    slf.close()
    
if __name__ == '__main__':
    main(user_file, song_file, target_file)
