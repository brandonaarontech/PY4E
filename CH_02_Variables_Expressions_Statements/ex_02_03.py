################################################################################
# Name: Brandon A Bustamante
# Chapter: 02
# Exercise: 03
# Description: Write a program to prompt the user for hours and rate per hour 
# using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour 
# to test the program (the pay should be 96.25). You should use input to read a 
# string and float() to convert the string to a number. Do not worry about error 
# checking or bad user data.
# Input: hours = 35, rate = 2.75
# Output: Pay 96.25
################################################################################

hours = input("Enter Hours:")
rate_per_hour = input("Enter Rate:")

hours = float(hours)
rate_per_hour = float(rate_per_hour)

gross_pay = hours * rate_per_hour

print("Pay:", gross_pay)
