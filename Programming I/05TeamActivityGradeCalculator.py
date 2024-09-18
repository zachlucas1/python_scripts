#Title: Grade Calculator
#Author: Zach Lucas
#Description: User inputs grade percentages

grade = int(input('What is your grade percent? '))

#If and Elif statements for grade
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
elif grade >= 50:
    letter = 'F'

#+ or - sign for after the grade
last_digit = grade % 10

if last_digit >= 7:
    sign = '+'
if last_digit < 3:
    sign = '-'

print(f'Your letter grade is: {letter}{sign}')

if grade >= 60:
    print('Congratulations! You passed the class!')
else:
    print('You did not pass the class, stay focused next time!')