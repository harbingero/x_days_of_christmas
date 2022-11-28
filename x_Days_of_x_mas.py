import random
import re
giftList = []
reverseThisList = []
entire_song = []
clear = ""
add_to_song = ""
number_days = ("first",
               "second",
               "third",
               "fourth",
               "fifth",
               "sixth",
               "seventh",
               "eighth",
               "ninth",
               "tenth",
               "eleventh",
               "twelfth",
               "thirteenth",
               "fourteenth",
               "fifteenth",
               "sixteenth",
               "seventeenth",
               "eighteenth",
               "nineteenth",
               "twentieth",
               "twenty-first",
               "twenty-second",
               "twenty-third",
               "twenty-fourth")
song_days = ("",
             "Two",
             "Three",
             "Four",
             "Five",
             "Six",
             "Seven",
             "Eight",
             "Nine",
             "Ten",
             "Eleven",
             "Twelve",
             "Thirteen",
             "Fourteen",
             "Fifteen",
             "Sixteen",
             "Seventeen",
             "Eighteen",
             "Nineteen",
             "Twenty",
             "Twenty-one"
             "Twenty-two",
             "Twenty-three",
             "Twenty-four")
path_to_song = "12_Days_of_Christmas_2022_Song.txt"
path_to_list = "12_Days_of_Christmas_2022_List.txt"
song_add = " day of Christmas my true love gave to me!\n"
regex_number = "^[)0-12+(]"
regex_on_the = "^On the"
lines = "-----------------------------------------------------------------\n"
increment = 0
temp = 0
on_day = 0
check = False
in_numbers = False
after_lines = False
to_be_cleared = False  # Clear song file
recite_song = True  # Print song to terminal
write = True  # True to add to song

# Check the song to see what day we're on
with open(path_to_song, "r") as f2:
    for x in f2:
        entire_song.append(x)
    for x in range(len(number_days)):
        for y in range(len(entire_song)):
            if len(entire_song) == 0:
                on_day = 0
                break
            if number_days[x].lower() not in entire_song[y].lower():
                pass
            else:
                on_day = x + 1
                break


for i in entire_song:
    regex_check = re.search(regex_on_the, i)
    regex_line = re.search(lines, i)
    if regex_line and increment < len(entire_song)-1:
        reverseThisList = []
    elif not regex_line and not regex_check and len(i) > 1:
        reverseThisList.append(i.strip() + "\n")
    increment += 1

reverseThisList.reverse()

# on_day is now set to what the song is on.
with open(path_to_list, "r") as f1:
    for i in f1:
        strippedI = i.strip()
        regex_check = re.search(regex_number, strippedI)
        if regex_check:
            in_numbers = True
            if str(on_day+1) in strippedI:
                check = True
            elif str(on_day+2) in strippedI:
                break
            else:
                pass
        if in_numbers is False and len(strippedI) > 0 and on_day > 0:
            giftList.append(strippedI)
        if in_numbers and not regex_check and check and len(strippedI) > 0:
            giftList.append(strippedI)

# items are now filled with the potential of being random, now add it to the song.
with open(path_to_song, "a") as f3:
    song_Line = ""
    add_to_song = giftList[random.randint(0, len(giftList)-1)]
    for line in entire_song:
        while re.search(add_to_song, line):
            add_to_song = giftList[random.randint(0, len(giftList))]
    if len(entire_song) > 0:
        song_Line = "\n"
        song_Line = song_Line + "On the " + number_days[on_day] + song_add + song_days[on_day] + " " + add_to_song + "\n"
    else:
        song_Line = song_Line + "On the " + number_days[on_day] + song_add + song_days[on_day] + add_to_song + "\n"
    for append in reverseThisList:
        song_Line += append
    if write:
        f3.write(song_Line + lines)

# Reciting song to terminal if above variable is True
if recite_song:
    with open(path_to_song) as f4:  # Displays in terminal
        for line in f4:
            print(line.strip())

# Clear reset the song file if variable is True
if to_be_cleared:
    clear = input("Clear file?")  # Clear file within terminal
if len(clear) > 0:
    with open(path_to_song, "w") as f5:
        f5.write("")
