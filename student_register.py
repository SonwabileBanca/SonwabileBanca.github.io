# Display
print('Welcome to the \033[034mExam Portal\033[0m what would you like to write\n')

#How many students are entering
students = int(input('How many \033[035mstudents\033[0m are registering:'))
#Open the txt file 
with open("reg_form.txt", "w") as f:
    
    for x in range(students):
    
        student = input(f"Enter your ID number {x+1}: ")
        f.write(f"Student {x+1}: {student}\t..........\n")
    f.close()
        

    




