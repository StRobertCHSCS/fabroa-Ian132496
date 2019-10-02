'''
-------------------------------------------------------------------------------
Name:		Problem2.py
Purpose:    Finding the number of pieces of chicken each student and Mr. Fabroa gets 

Author:	Cho.S

Created:	date in 02/10/2019
-------------------------------------------------------------------------------
'''

# get the number of chicken pieces from the user
chicken_pieces = int(input("Enter the number of chicken pieces: "))

# get the number of students from the user
students = int(input("Enter the number of students in the class: ")) 

# find how many pieces each student gets
pieces_per_student = int(chicken_pieces//students)

# find how many pieces Mr. Fabroa gets
Mr_Fabroa = int(chicken_pieces % pieces_per_student)

# output the number of pieces each student gets
print(pieces_per_student)

#output the number of pieces Mr.Fabroa gets
print(Mr_Fabroa)