"""good_input = False

while not good_input:

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        age = 0
        print('Bad error!')

    else:
        good_input = True
        try:
            nextYear = age + 1
            print(f'Next year you will be {nextYear} old.')
        #instead of crashing it just prints this if try doesn't work
        except TypeError as error_message:
            print(error_message)
            print('Something went wrong')"""

"""data = [3, 4, 5, 'x', 15, 9]

def tally_number(the_number, current_total):
    new_total = current_total + the_number
    return new_total

def process_list(list_of_numbers):
    total = 0
    count = 0
    for item in list_of_numbers:
        try:
            total = tally_number(item, total)
            count = count + 1
        except Exception as ex:
            print(f'Something went wrong adding {item} to {total}.')

    average = total / count

    print(f'The total is {total}.')
    print(f'The average is {average:.2f}')

def main():
    process_list(data)

main()"""

######

#syntax error
"""x = 42
y = 206
if x == y
    print('Success!')"""

#runtime error
"""x = 42
y = 0
print(x / y)"""

#catching runtime errors
"""x = 42
y = 0

print()
try:
    print(x / y)

except ZeroDivisionError as ex:
    print('Sorry something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This is the cleanup code')
print()"""

#logic error
#this code will not run at all
"""x = 206
y = 42
if x < y:
    print(f'{str(x)} is greater than {str(y)}')"""


def main():
    try:
        gender = input("Enter your gender (M or F): ")

        weight = get_float("Enter your weight in kilograms: ")
        height = get_float("Enter your height in centimeters: ")
        age = get_float("Enter your age in years: ")

        bmr = basal_metabolic_rate(gender, weight, height, age)
        print(f"Your basal metabolic rate is {bmr} calories per day.")

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")


def get_float(prompt):
    """Get a number from the user, validate that the user entered
    a number and not some other text, and return the number. If
    the user enters an invalid number, this function will prompt
    the user repeatedly until the user enters a valid number.

    param prompt: A string to display to the user.
    return: The number entered by the user.
    """
    while True:
        try:
            text = input(prompt)
            number = float(text)
            break
        except ValueError:
            print(f"{text} is not a number.")
            print("Please enter a number.")

    return number


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr)
    in calories per day. weight must be in kilograms, height must
    be in centimeters, and age must be in years.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()