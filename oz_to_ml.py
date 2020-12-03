'''
-------------------------------------------------------------------------------
Name:		oz_to_ml.py
Purpose:	Changing the amount of fluid ounces to millilitres and giving the proper amount for number of servings.

Author:	Huang.S

Created:	date in 02/12/2020
------------------------------------------------------------------------------
'''

# inputing the amount of fluid ounces and servings
ounces = float(input("Enter ounces per 4 servings: "))
servings = float(input("Enter number of servings: "))

# changing oz to ml
ml = (ounces /4 *29.5735 *servings)

# output
print("You will need " + str(ml) + "ml") 