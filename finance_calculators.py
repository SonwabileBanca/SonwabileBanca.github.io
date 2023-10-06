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














