import os
import random

user_file = os.getcwd() + '\\raw-files\\user_v1.csv'
song_file = os.getcwd() + '\\raw-files\\song_v1.csv'
target_file = os.getcwd() + '\\raw-files\\song_likes_v1.csv'


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
        
        # Some lines fail the decoding, but there isn't enough time to
        # troubleshoot, so I'm using this as a workaround...
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
    userct = 0
    
    for line in userf:
        username = str(line).split(',')[0]
       
        song_lines = " "
        while song_lines == " ":
            song_lines = get_random_lines(songf, 5)
        
        for i in range(len(song_lines)):
            song_id = song_lines[i].split(',')[0]
            song_count = str(random.randint(0, 100))
            slf.write(bytes(song_id + delim + username + delim + song_count +
                delim + str(random.randint(3, 5)) + '\r\n', 'utf-8'))
            # For the rating, we pick random float b/w 3 and 5


    userf.close()
    songf.close()
    slf.close()
    
if __name__ == '__main__':
    main(user_file, song_file, target_file)
