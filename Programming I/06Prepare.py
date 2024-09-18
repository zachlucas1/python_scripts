"""gpa = float(input('What is your GPA? '))
lowest_grade = float(input('What is your lowest grade? '))

if gpa >= .85 and lowest_grade >= .70:
    honor_roll = True
else:
    honor_roll = False

if honor_roll:
    print('Well done!')
else:
    print('You did not make honor roll.')"""

#-----------------------------------------------------

"""if gpa >= .85: 
    if lowest_grade >= .70:
        print('You made the honor roll!')
    else:
        print('You did not make the honor roll.')"""

#-----------------------------------------------------

x = 7
y = 9

if x > 5 and y > 10:
    print('True')
else:
    print('False')

if x > 5 or y > 10:
    print('True')
else:
    print('False')

#-----------------------------------------------------

is_hot = True

# Using the "not" keyword
if not is_hot:
    print("It is not hot")

# It works, but is generally avoided to check if it is false:
if is_hot == False:
    print("It is not hot")
