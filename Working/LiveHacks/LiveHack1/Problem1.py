'''
-------------------------------------------------------------------------------
Name:		Problem1.py

Purpose:    Finding Fahrenheit from Celsius

Author:	Cho.S

Created:	date in 02/10/2019
-------------------------------------------------------------------------------
'''

# get Celsius from user
Celsius = float(input("Enter the Celsius: "))

# compute Farenheit from Celsius
Fahrenheit = ((9/5) * Celsius) + 32

# output Fahrenheit
print("The temperature in Fahrenheit is " + str(Fahrenheit))
