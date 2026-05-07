################################################################################
# Name: Brandon A Bustamante
# Chapter: 10
# Exercise: 02
# Description: 10.2 Write a program to read through the mbox-short.txt and figure 
# out the distribution by hour of the day for each of the messages. You can pull 
# the hour out from the 'From ' line by finding the time and then splitting the 
# string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 
# 09:14:16 2008 Once you have accumulated the counts for each hour, print out the 
# counts, sorted by hour as shown below.
# Input: mbox-short.txt
# Output: 
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
################################################################################

try:
    input_file = open("mbox-short.txt")

except:
    print('File not found')
    quit()

hours = {}

for line in input_file:
    if line.startswith('From '):
        line_text = line.split()
        time = line_text[5]
        hour_min_sec = time.split(':')
        hour = hour_min_sec[0]

        hours[hour] = hours.get(hour, 0) + 1

hours_list = list()
for key,val in list(hours.items()):
    hours_list.append((key, val))

hours_list.sort()

for key, val in hours_list:
    print(key, val)
