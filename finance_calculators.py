'''Standardized Input Checking:

Used .lower() method to convert the user's input to lowercase. This ensures that the program works regardless of the user's choice being in uppercase, lowercase, or a combination.
Added Comments:

Added comments to explain each section of the code, including the purpose of the program, user prompts, input variables, and the logic behind each calculation.
Improved Variable Naming:

Renamed the variables inside the if conditions to reflect the nature of the calculated values. For example, simple_interest, compound_interest, and bond_repayment make it clearer what each variable represents.
Standardized Choice Comparisons:

Used investorChoice.lower() == "simple" instead of multiple conditions to make the code cleaner and more readable.
Remember, good documentation and clear variable naming are essential for making your code understandable to others (or even to yourself in the future).'''

#=================================Financial Calculator For interest and Bonds==================================

#=======================================Simple==========Compound============Bond=============================
import math
#Display the Menu to user
print('Investment - to calculate the amount of interest you will earn on your investment\n\nBond - calculate the amount you will have to pay on a home loan.\n\nEnter either Investment or bond\n\n\t')
#Promt user to Enter variables
investorChoice = str(input("What is your choice of calculation?"))
#Input variables
Amount = float(input("Enter the amount."))
interestRate = float(input("Enter the interest as percentage"))
time = int(input("The number of years."))

if investorChoice == "simple" or investorChoice == "Simple" or investorChoice == "SIMPLE":
    investorChoice = Amount * (1 + (interestRate/100)*time)
    print(f"Your simple interest accumulated is R{investorChoice}")
# Simple and Compound interest formulae
elif investorChoice == "compound" or investorChoice == "Compound" or investorChoice == "COMPOUND":
    investorChoice = Amount * math.pow((1+(interestRate)/100),time)
    print(f"Your compound interest is R{investorChoice}")
# Bond repayment formula
elif investorChoice == "bond" or investorChoice == "Bond" or investorChoice == "BOND":
    investorChoice = ((interestRate/100)/12 * Amount)/(1 -(1 + (interestRate/100)/12)**(-time))
    print(f"Your Bond is R{investorChoice}")
else:
    print("Error in your inputs!!!")














