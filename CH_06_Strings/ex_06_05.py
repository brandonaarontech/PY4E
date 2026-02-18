################################################################################
# Name: Brandon A Bustamante
# Chapter: 06
# Exercise: 05
# Description: Write code using find() and string slicing (see section 6.10) to 
# extract the number at the end of the line below. Convert the extracted value 
# to a floating point number and print it out.
# Input: text = "X-DSPAM-Confidence:    0.8475"
# Output: 0.8475
################################################################################

text = "X-DSPAM-Confidence:    0.8475"

starting_point = text.find("0")

number = text[starting_point:]

number = float(number)

print(number)