'''
-------------------------------------------------------------------------------
Name:		Practice1.py
Purpose:    Finding Celsius from Fahrenheit

Author:	Cho.S

Created:	date in 01/10/2019
------------------------------------------------------------------------------
'''

# get fahrenheit from user
fahrenheit = float(input("Enter the Fahrenheit: "))

# compute celsius from fahrenheit 
celsius = (5/9) * (fahrenheit - 32)

# output celsius 
print("The temperature in celsius is " + str(celsius))