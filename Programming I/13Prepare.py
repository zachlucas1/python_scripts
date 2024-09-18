######

"""from datetime import datetime

def print_time():
    print('Task completed')
    print(datetime.now())
    print()

first_name = 'Susan'
print('first name assigned')
print(datetime.now())
print()

for x in range (0, 10):
    print(x)
print('loop completed')
print(datetime.now())
print()

name_ask = input('What is your name? ').capitalize()

print(f'Your name is {name_ask}.')
print_time()"""

######

"""def get_initial(name):
    initial = name[0:1].capitalize()
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print(f'Your initials are: {get_initial(first_name)}/
{get_initial(last_name)}.')"""

######

"""def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].capitalize()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

print(f'Your initial is: {first_name_initial}')"""

######

"""def print_message():
    print('Hello CSE 110 World!')
    print()

print_message()

print_message()"""

######

"""def print_double(value):
    double_value = value * 2
    print(double_value)

print_double(12)
print_double(3)
print_double(42)"""

######

"""def get_double(value):
    double_value = value *2
    return double_value

new_number = get_double(4)
print(new_number)"""

######

def print_message(the_message):
    print(the_message)

the_message = 'Message 1'
print_message(the_message)

user_message = 'Message 2'
print_message(user_message)