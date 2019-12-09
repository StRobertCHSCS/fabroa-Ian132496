'''
------------------------------------------------------------------------------
Name:	    livehack3_problem1.py
Purpose:    to find the number of heating days

Author:	Cho.S

Created:	09/12/2019
------------------------------------------------------------------------------
'''

print("****** Heating Days Tracker ******")

number_days = int(input("Enter the number of days to track: "))
heating_days = 0

for i in range(number_days):
    temperature = int(input("temperature: "))
    if temperature < 15:
        heating_days += 1

print("There are", heating_days, "heating days")
