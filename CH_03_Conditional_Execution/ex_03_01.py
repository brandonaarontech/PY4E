################################################################################
# Name: Brandon A Bustamante
# Chapter: 03
# Exercise: 01
# Description: Write a program to prompt the user for hours and rate per hour 
# using input to compute gross pay. Pay the hourly rate for the hours up to 40 
# and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 
# hours and a rate of 10.50 per hour to test the program (the pay should be 
# 498.75).You should use input to read a string and float() to convert the 
# string to a number. Do not worry about error checking the user input - assume 
# the user types numbers properly.
# Input: hours = 45, rate_per_hour = 10.50
# Output: 498.75
################################################################################

hours = input("Enter Hours:")
rate_per_hour = input("Enter Rate:")
overtime_hours = 0

hours = float(hours)
rate_per_hour = float(rate_per_hour)

if hours >= 40:
    overtime_hours = hours - 40
    hours = hours - overtime_hours

normal_pay = hours * rate_per_hour

overtime_rate = rate_per_hour * 1.5
overtime_pay = overtime_hours * overtime_rate

gross_pay = normal_pay + overtime_pay

print(gross_pay)
