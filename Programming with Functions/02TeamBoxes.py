"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python program
named boxes.py that asks the user for two integers: 1) the number of
items and 2) the items per box. Your program must require the user to
enter positive integers and then must compute and print the number of
boxes necessary to hold the items.
"""

import math

#This will change to True after the user enters a valid non-zero
# integer
stop = False

#minimum and maximum intigers that may be entered
minimum = 1

# asks user for an integer until they enter something greater
# than or equal to minimum
while not stop:
    text = input('Enter the number of items: ')
    
    # determine if they are decimals
    if text.isdecimal():
        
        #convert inputted string to an integer
        number_items = int(text)
        if number_items < minimum:
            print(f'"{number_items}" is too small. Please enter another positive integer.')
        else:
            stop = True
    else:
        print(f'"{text}" is not a positive integer. Please enter a positive integer.')

print()

stop = False

minimum = 1

while not stop:
    text = input('Enter the number of items per box: ')
    if text.isdecimal():
        per_box = int(text)
        if per_box < minimum:
            print(f'"{per_box}" is too small. Please enter another positive integer.')
        else:
            stop = True
    
    else:
        print(f'"{text}" is not a positive integer. Please enter a positive integer.')

print()

num_boxes = math.ceil(number_items / per_box)

print(f'For {number_items} items, packing {per_box} items in each box, you will need {num_boxes} boxes.')
    #print(f'For {items} items, packing {text} items in each box, you will need {} boxes.')