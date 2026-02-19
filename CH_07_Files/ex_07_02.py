################################################################################
# Name: Brandon A Bustamante
# Chapter: 07
# Exercise: 02
# Description:  Write a program that prompts for a file name, then opens that 
# file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.
# Input: mbox-short.txt
# Output: Average spam confidence: 0.7507185185185187
################################################################################

# Use the file name mbox-short.txt as the file name
try:
    fname = input("Enter file name: ")
    fh = open(fname)
except:
    print("File not found")
    quit()

line_count = 0
total = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        line_count += 1
        starting_point = line.find("0")
        cur_number = float(line[starting_point:])
        total += cur_number

avg = total / line_count

print("Average spam confidence:", avg)
