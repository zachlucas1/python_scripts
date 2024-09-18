"""import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.datetime.now())
    print()

first_name = 'susan'
print_time('printed first name')

for x in range(0, 10):
    print(x)
print_time('completed for loop')"""

def get_initial(name):
    initial = name[0:1].upper() #the [0:1] tells it which letter to pick
    return initial

first_name = input('What is your first name? ')
first_name_initial = get_initial(first_name)

middle_name = input('What is your middle name? ')
middle_name_initial = get_initial(middle_name)

last_name = input('What is your middle name? ')
last_name_initial = get_initial(last_name)

print(f'Your initials are {first_name_initial}{middle_name_initial}{last_name_initial}')

"""def get_initial(name, force_uppercase=True): #this automatically forces it to be uppercase unless otherwise specified
    if force_uppercase:
        initial = name[0:1].upper() #the [0:1] tells it which letter to pick
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False) #False specifies that it will not be uppercase

print(f'Your initial is {first_name_initial}')"""

"""# Define a function that accepts one parameter.
#
# Whatever argument is passed to this function
# when it is called, will be stored in the
# "numbers"  parameter, and will be accessible
# within the body of this function.
def print_average(numbers):
    # Compute and print the average of the
    # numbers stored in the numbers list.

    # param numbers: A list of numbers
    # return: Nothing
    
    total = 0
    for number in numbers:
        total += number

    average = total / len(numbers)
    print(f"The average is: {average}")"""

"""# Define a function that accepts one parameter.
def calculate_average(numbers):
    # Compute and return the average of the
    # numbers stored in the numbers list.

    # param numbers: A list of numbers
    # return: The average value of the numbers
    
    total = 0
    for number in numbers:
        total += number

    average = total / len(numbers)

    # The returned result will be available
    # wherever this function was called.
    return average"""

# Define a function that accepts one parameter.
def calculate_average(numbers):
    """Compute and return the average of the
    numbers stored in the numbers list.

    param numbers: A list of numbers
    return: The average value of the numbers
    """
    total = 0
    for number in numbers:
        total += number

    average = total / len(numbers)

    # The returned result will be available
    # wherever this function was called.
    return average


# Define the main function.
def main():
    # Create a list of numbers.
    scores = [100, 90, 85, 84, 99]

    # Call the calculate_average function and store
    # its return value in a variable to use later.
    final_grade = calculate_average(scores)

    if final_grade >= 93:
        print("You got an A 🤩")
    else:
        print("You did not get an A 😞")


# Start this program by
# calling the main function.
main()