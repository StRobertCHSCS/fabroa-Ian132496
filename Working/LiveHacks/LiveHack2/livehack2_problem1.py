'''
------------------------------------------------------------------------------
Name:	    livehack2_problem1.py
Purpose:    to compute and find cash bonus

Author:	Cho.S

Created:	18/11/2019
------------------------------------------------------------------------------
'''

# get marks, earnings
mid_term = float(input("Enter mid term average: "))
final_average = float(input("Enter final average: "))

# calculate the amount of cash bonus
if final_average - mid_term >= 0.01:
    final_average - mid_term <= 0.05
    print("Congratulations, the cash bonus is $100")

elif final_average - mid_term >= 0.06:
    final_average - mid_term <= 0.9
    print("Congratulations, the cash bonus is $300")

elif final_average - mid_term >= 0.1:
    print("Congratulations, the cash bonus is $600")

else:
    print("Sorry, no cash bonus for your class.")
