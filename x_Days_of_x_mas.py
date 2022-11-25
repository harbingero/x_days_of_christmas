import random
import re
giftList = []
path_to_song = "12_Days_of_Christmas_2022_Song.txt"
path_to_list = "12_Days_of_Christmas_2022_List.txt"
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
               "twelfth")
reverseThisList = []
song_days = ("", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve")
on_day = 0
entire_song = []
song_add = " day of Christmas my true love gave to me!\n"
add_to_song = ""
regex_number = "^[)0-12+(]"
check = False
in_numbers = False
lines = "-----------------------------------------------------------------\n"
after_lines = False

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
    #Set up check regex start on the, or line to append not on the or line to a reverseThisList, and line resets reverseThisList unless on end of document

# on_day is now set to what the song is on.  Now we need to add one to get the next verse of the song.
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
    print(entire_song)  # This area, I am attempting to fix for formatting.  The song kind of works.  Now I need it to go backwards 5,4,3,2,and an x
    if len(entire_song) > 0:
        song_Line = "\n"
        song_Line = song_Line + "On the " + number_days[on_day] + song_add + song_days[on_day] + " " + add_to_song + "\n"
    else:
        song_Line = song_Line + "On the " + number_days[on_day] + song_add + song_days[on_day] + add_to_song + "\n"
    f3.write(song_Line + lines)

# with open(path_to_song) as f4: #Displays in terminal
#     for line in f4:
#         print(line.strip())

# clear = input("Clear file?") #Clear file within terminal
# if len(clear) > 0:
#     with open(path_to_song,"w") as f5:
#         f5.write("")
