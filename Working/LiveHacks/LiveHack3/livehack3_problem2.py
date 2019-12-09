'''
------------------------------------------------------------------------------
Name:	    livehack3_problem2.py
Purpose:    to compute the average distance driven per day

Author:	Cho.S

Created:	09/12/2019
------------------------------------------------------------------------------
'''

print("***** Welcome to the Distance Tracker ******")

distance = 0
day_count = 0
total_distance = 0

while total_distance <= 100:
    distance = float(input("Enter the distance travelled for the day: "))
    total_distance = total_distance + distance
    day_count += 1

average_driven = total_distance/day_count

print("it took", str(day_count), "days to surpass 100km driven.")
print("the average distance driven per day is " + str(average_driven))
