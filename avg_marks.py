'''
-------------------------------------------------------------------------------
Name:		avg_marks.py
Purpose:	The average mark between four courses

Author:	Huang.S

Created:	date in 02/12/2020
------------------------------------------------------------------------------
'''

# get 4 marks from the UserWarning
mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))
mark4 = float(input("Enter mark 4: "))

# compare the average of the 4 marks
marks_avg = (mark1 + mark2 + mark3 + mark4)/4

# output the average
print("The average of the 4 marks is " + str(marks_avg))
