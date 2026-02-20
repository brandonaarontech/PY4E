################################################################################
# Name: Brandon A Bustamante
# Chapter: 08
# Exercise: 04
# Description: Open the file romeo.txt and read it line by line. For each line, 
# split the line into a list of words using the split() method. The program 
# should build a list of words. For each word on each line check to see if the 
# word is already in the list and if not append it to the list. When the program 
# completes, sort and print the resulting words in python sort() order as shown 
# in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt
# Input: romeo.txt
# Output: 
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 
# 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 
# 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
################################################################################

word_list = list()


try:
    file = open("romeo.txt")

except:
    print("File not found")
    quit()

for line in file:
    words = line.split()
    for word in words:
        if word not in word_list:
            word_list.append(word)

word_list.sort()

print(word_list)

