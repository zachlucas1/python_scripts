### INTEREST ###
"""# get account balance number from user
balance = float(input('Please enter an account balance: '))

# if balance is greater than 500 then compute intrest
if balance > 500:
    interest = balance * 0.03
    balance += interest

#print the balance
print(balance)"""

### DISCOUNT RATE ###
"""#get cost rate from user
cost = float(input('Please enter the cost: '))

if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

#compute discount
discount = cost * rate
cost -= discount

#print discounted cost
print(f'After the discount you will pay {cost}')"""

### MEMBERSHIP OPERATOR ###
"""#set that contains family names
surnames = {"Smith", "Lopez", "Marsh", "Olsen", "Vasiuk"}

#get the users family name
family = input('Please enter your family name: ')

#determine if user's family name is in the set of family names
if family in surnames:
    print('Your family name is in the set.')
else:
    print('Your family is NOT in the set.')"""

### RANGE OF NUMBERS ###
"""#count from zero to nine by ones.
for i in range(10):
    print(i)

#count from zero to eight by twos
for i in range(0, 10, 2):
    print(i)

#count from 100 down to 70 by three.
for i in range (100, 69, -3):
    print(i)"""

### DIFFERENT TYPES OF LOOPS ###
"""#list
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]

#set
names = {"Smith", "Lopez", "Marsh", "Olsen", "Vasiuk"}

#dictionary
students = {
    "67-412-8350" : "Alan Benson",
    "76-240-1835" : "Madison Silverlake",
    "06-412-7583" : "Samyukta Daniels"
}

#print each value in the list
for color in colors:
    print(color)

#print each value in a set
for family in names:
    print(family)

#print each key value pair in a dictionary.
for inumber, name in students.items():
    print(inumber, name)"""

### BREAK STATEMENT ###
# Get ten or fewer numbers from the user and add them
# together. Notice that this loop uses underscore (_) as
# the counting variable, which is a valid variable name.
# Many programmers use underscore to indicate that the
# variable will not be used within the body of the loop.
sum = 0
for _ in range(10):
    n = float(input("Please enter a number: "))
    if n == 0:
        break
    sum += n
print(sum)

### ```PRACTICE``` ###
### CONDITIONAL lOGIC ###

"""if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)

country = 'canada'
if country.lower() == 'canada':
    print('Oh look a Canadian!')
else:
    print('You are not from Canada.')"""

### HANDLING MULTIPLE CONDITIONS ###

"""if country.lower() == 'Canada'
    if province.lower() == 'Alberta' or == 'Nunavut':
        tax= 0.05
    elif province.lower() == 'Ontario':
        tax= 0.13
    else:
        tax = 0.15
else:
    tax = 0.0"""

### COMPLEX CONDTIONS ###

"""if gpa >= .85 and lowest_grade >= .70:
    print('Well done')

#this also works#
if gpa >= .85 and lowest_grade >= .70:
    honor_roll = True
else:
    honor_roll = False
if honor_roll:
    print('Well done')"""

### COLLECTIONS ###

"""names = ['Christopher', 'Susan']
scores = []
scores.append(98) # Add new item to the end
scores.append(99)
print(names)
print(scores)
print(scores[1]) # Collections start at zero

from array import array
scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])"""

### VALIDATING USER INPUT ###

# The minimum and maximum integers that the user may enter.
minimum = 20
maximum = 40

# Make a boolean variable that will change to
# True after the user enters a valid integer.
valid = False

# Repeatedly ask the user to enter an integer until the
# user enters one between minimum and maximum, inclusive.
while not valid:
    text = input(f"Enter an integer between {minimum} and {maximum}: ")

    # Determine if all the characters that
    # the user entered are decimal digits.
    if text.isdecimal():

        # Convert the text that the user
        # entered from a string to an integer.
        integer = int(text)

        # Determine if the integer entered by the
        # user is between minimum and maximum, inclusive.
        if integer < minimum:
            print(f"{integer} is too small. Please"
                    " enter another positive integer.")
        elif integer > maximum:
            print(f"{integer} is too large. Please"
                    " enter another positive integer.")
        else:
            # If the computer gets to this line of code,
            # the user entered an integer between minimum
            # and maximum, so change the boolean variable
            # to True so that the loop will stop repeating.
            valid = True

    else:
        # The user entered at least one character that is not a decimal
        # digit, so print a message asking the user to enter an integer.
        print(f"'{text}' is not a positive integer."
                " Please enter a positive integer.")

# Use the integer in the program.
print(integer)