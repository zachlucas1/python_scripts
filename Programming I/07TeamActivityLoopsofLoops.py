#Title: Team Loop Multiplication Table Activity
#Author: Zach Lucas
#Description: Asks user for number rows and outputs a multiplication table

#Asks user for how they want their multiplication table
user_choice = int(input('How many colummns and rows do you want in your multiplication table? '))

range_size = user_choice + 1 

#Number of rows
for row_number in range(1, range_size):
    
    #Number of columns
    for col_number in range (1, range_size):
        number = row_number * col_number
        print(f'{number:3}', end=' ')
    print()