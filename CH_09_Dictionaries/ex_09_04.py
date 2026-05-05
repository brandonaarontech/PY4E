################################################################################
# Name: Brandon A Bustamante
# Chapter: 09
# Exercise: 04
# Description: Write a program to read through the mbox-short.txt and figure out 
# who has sent the greatest number of mail messages. The program looks for 
# 'From ' lines and takes the second word of those lines as the person who sent 
# the mail. The program creates a Python dictionary that maps the sender's mail 
# address to a count of the number of times they appear in the file. After the 
# dictionary is produced, the program reads through the dictionary using a 
# maximum loop to find the most prolific committer.
# Input: mbox-short.txt
# Output: cwen@iupui.edu 5
################################################################################

try:
    file = open("mbox-short.txt")

except:
    print("File not found")
    quit()

words = []
emails = dict()

for line in file:
    if 'From ' in line:
        words = line.split()
    
        emails[words[1]] = emails.get(words[1],0) + 1

max_count = 0
max_email = ''

for email in emails:
    if max_count < emails[email]:
        max_count = emails[email]
        max_email = email

print(max_email, max_count)