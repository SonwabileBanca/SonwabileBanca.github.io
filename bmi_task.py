


#Request weight and hight in (m)
weight = float(input("Enter your weight:"))
height = float(input("Enter your height in (m)"))
#use the BMI formula to calcuate
BMI = weight/(height)**2

if BMI >= 30:
    
#print out the BMI obese
    print("User is Obese")

elif BMI >= 25:

#print out the BMI overveight
    print("User is Overweight")

elif BMI >= 18.5:

#print out the BMI normal
    print("User is Normal")

elif BMI < 18.5:

#print BMI underweight
    print("You are Underweight")